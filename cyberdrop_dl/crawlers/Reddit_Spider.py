from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING, Dict, List

import asyncpraw
from aiolimiter import AsyncLimiter
from yarl import URL

from ..base_functions.base_functions import get_filename_and_ext, log, logger, make_title_safe, create_media_item
from ..base_functions.data_classes import DomainItem, MediaItem
from ..base_functions.error_classes import NoExtensionFailure

if TYPE_CHECKING:
    from ..base_functions.base_functions import ErrorFileWriter
    from ..base_functions.sql_helper import SQLHelper
    from ..client.client import ScrapeSession


class RedditCrawler:
    def __init__(self, session: ScrapeSession, scraping_mapper, separate_posts: bool, quiet: bool, SQL_Helper: SQLHelper,
                 error_writer: ErrorFileWriter, args: Dict[str, str]):
        self.separate_posts = separate_posts
        self.quiet = quiet
        self.SQL_Helper = SQL_Helper
        self.limiter = asyncio.Semaphore(1)

        self.scraping_mapper = scraping_mapper
        self.error_writer = error_writer

        self.reddit_personal_use_script = args["Authentication"]["reddit_personal_use_script"]
        self.reddit_secret = args["Authentication"]["reddit_secret"]
        self.reddit = asyncpraw.Reddit(client_id=self.reddit_personal_use_script,
                                       client_secret=self.reddit_secret,
                                       user_agent="CyberDrop-DL",
                                       check_for_updates=False)

    async def fetch(self, url: URL) -> DomainItem:
        """Basic director for actual scraping"""
        domain_obj = DomainItem("reddit", {})
        try:
            if "i.redd.it" in url.host:
                try:
                    media_item = await create_media_item(url, url, self.SQL_Helper, "reddit")
                except NoExtensionFailure:
                    logger.debug("Couldn't get extension for %s", url)
                    return domain_obj
                await domain_obj.add_media("Loose Reddit Files", media_item)

            async with self.limiter:
                log(f"Starting: {url}", quiet=self.quiet, style="green")
                if "user" in url.parts or "u" in url.parts:
                    await self.get_user(url, domain_obj)
                elif "r" in url.parts:
                    await self.get_subreddit(url, domain_obj)

            await self.SQL_Helper.insert_domain("reddit", url, domain_obj)
            log(f"Finished: {url}", quiet=self.quiet, style="green")
        except Exception as e:
            logger.debug("Error encountered while handling %s", url, exc_info=True)
            await self.error_writer.write_errored_scrape(url, e, self.quiet)

        return domain_obj

    async def handle_external_links(self, content_links: List, referer: URL) -> None:
        """Maps external links to the scraper class"""
        tasks = [asyncio.create_task(self.scraping_mapper.map_url(link, title, referer)) for link, title in content_links]
        if tasks:
            await asyncio.wait(tasks)

    async def handle_media(self, media_url: URL, referer: URL, title: str, domain_obj: DomainItem) -> None:
        try:
            media_item = await create_media_item(media_url, referer, self.SQL_Helper, "reddit")
        except NoExtensionFailure:
            logger.debug("Couldn't get extension for %s", media_url)
            return
        await domain_obj.add_media(title, media_item)

    async def get_posts(self, title: str, url: URL, domain_obj: DomainItem, submissions):
        submissions = [submission async for submission in submissions]

        external_links = []
        for submission in submissions:
            media_url = URL(submission.url)
            if self.separate_posts:
                temp_title = title + "/" + await make_title_safe(submission.title)
            else:
                temp_title = title

            if "i.redd.it" in media_url.host:
                await self.handle_media(media_url, url, temp_title, domain_obj)
            elif "gallery" in media_url.parts:
                links = await self.handle_gallery(submission, title, domain_obj)
                for link in links:
                    await self.handle_media(link, url, temp_title, domain_obj)
            else:
                if not "reddit.com" in media_url.host:
                    external_links.append((media_url, temp_title))
        await self.handle_external_links(external_links, url)

    async def handle_gallery(self, submission, title: str, domain_obj: DomainItem):
        items = [item for item in submission.media_metadata.values() if item["status"] == "valid"]
        links = []
        for item in items:
            links.append(URL(item["s"]["u"]).with_host("i.redd.it").with_query(None))
        return links

    async def get_user(self, url: URL, domain_obj: DomainItem):
        username = url.parts[-1] if url.parts[-1] != "" else url.parts[-2]
        title = await make_title_safe(username + " (Reddit)")

        user = await self.reddit.redditor(username)
        submissions = user.submissions.new(limit=None)
        await self.get_posts(title, url, domain_obj, submissions)

    async def get_subreddit(self, url: URL, domain_obj: DomainItem):
        subreddit = url.parts[-1] if url.parts[-1] != "" else url.parts[-2]
        title = await make_title_safe(subreddit + " (Reddit)")

        subreddit = await self.reddit.subreddit(subreddit)
        submissions = subreddit.new(limit=None)
        await self.get_posts(title, url, domain_obj, submissions)
