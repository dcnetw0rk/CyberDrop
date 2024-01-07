#!/opt/homebrew/bin/env python3
# coding=utf-8

import logging
from typing import Dict
from logging import Formatter, LogRecord

c2 = {
    "GOLD2": "\033[0m\033[38;5;186m",
    "GOLD2B": "\033[0m\033[1;38;5;186m",
    "SKY2": "\033[0m\033[38;5;153m",
    "LGREY": "\033[0m\033[38;5;252m",
    "NORMAL": "\033[0m\033[38;5;8m",
    "END": "\033[0m",
}


class color:
    # STANDARD COLORS (#30-37)
    BLACK = "\033[0m\033[38;5;232m"
    BLACKB = "\033[0m\033[1;38;5;232m"
    BLACK2 = "\033[0m\033[48;5;240m\033[38;5;231m"
    BLACK2B = "\033[0m\033[48;5;240m\033[1;38;5;231m"
    BLACK3 = "\033[0m\033[38;5;244m"
    BLACK3B = "\033[0m\033[1;38;5;244m"
    BLACK4 = "\033[0m\033[48;5;247m\033[38;5;232m"
    BLACK4B = "\033[0m\033[48;5;247m\033[1;38;5;232m"
    BLACK5 = "\033[0m\033[48;5;240m\033[38;5;214m"
    BLACK5B = "\033[0m\033[48;5;240m\033[1;38;5;214m"
    BLACK6 = "\033[0m\033[48;5;240m\033[38;5;153m"
    BLACK6B = "\033[0m\033[48;5;240m\033[1;38;5;153m"

    RED = "\033[0m\033[38;5;94m"
    REDB = "\033[0m\033[1;38;5;94m"
    RED2 = "\033[0m\033[38;5;202m"
    RED2B = "\033[0m\033[1;38;5;202m"
    RED3 = "\033[0m\033[38;5;28m"
    RED3B = "\033[0m\033[1;38;5;28m"

    IRED = "\033[0m\033[48;5;94m\033[38;5;231m"
    IREDB = "\033[0m\033[1;48;5;94m\033[1;38;5;231m"
    IRED2 = "\033[0m\033[48;5;202m\033[38;5;232m"
    IRED2B = "\033[0m\033[48;5;202m\033[1;38;5;232m"

    GREEN = "\033[0m\033[38;5;35m"  # SpringGreen4 00875f
    GREENB = "\033[0m\033[1;38;5;35m"  # SpringGreen4 00875f
    GREEN2 = "\033[0m\033[48;5;42m\033[38;5;232m"
    GREEN2B = "\033[0m\033[48;5;42m\033[1;38;5;232m"
    GREEN3 = "\033[0m\033[38;5;35m"
    GREEN3B = "\033[0m\033[1;38;5;35m"
    GREEN4 = "\033[0m\033[48;5;35m\033[38;5;232m"
    GREEN4B = "\033[0m\033[48;5;35m\033[1;38;5;232m"

    IGREEN = "\033[0m\033[48;5;29m\033[38;5;232m"
    IGREENB = "\033[0m\033[48;5;29m\033[1;38;5;232m"

    YELLOW = "\033[0m\033[38;5;191m"  # old: 47m
    YELLOWB = "\033[0m\033[1;38;5;191m"  # old: 47m
    YELLOW2 = "\033[0m\033[38;5;47m"
    YELLOW2B = "\033[0m\033[1;38;5;47m"
    YELLOW3 = "\033[0m\033[38;5;226m"
    YELLOW3B = "\033[0m\033[1;38;5;226m"
    YELLOW4 = "\033[0m\033[38;5;106m"
    YELLOW4B = "\033[0m\033[1;38;5;106m"

    IYELLOW = "\033[0m\033[48;5;191m\033[38;5;232m"
    IYELLOWB = "\033[0m\033[48;5;191m\033[1;38;5;232m"
    IYELLOW2 = "\033[0m\033[48;5;191m\033[38;5;32m"
    IYELLOW2B = "\033[0m\033[48;5;191m\033[1;38;5;32m"
    IYELLOW4 = "\033[0m\033[48;5;106m\033[38;5;232m"
    IYELLOW4B = "\033[0m\033[48;5;106m\033[1;38;5;232m"

    BLUE = "\033[0m\033[38;5;4m"
    BLUEB = "\033[0m\033[1;38;5;4m"
    BLUE2 = "\033[0m\033[48;5;4m\033[38;5;232m"
    BLUE2B = "\033[0m\033[48;5;4m\033[1;38;5;232m"
    BLUE3 = "\033[0m\033[38;5;91m"
    BLUE3B = "\033[0m\033[1;38;5;91m"
    BLUE4 = "\033[0m\033[48;5;91m\033[38;5;231m"
    BLUE4B = "\033[0m\033[1;48;5;91m\033[1;38;5;231m"

    GREY = "\033[0m\033[38;5;247m"
    GREYB = "\033[0m\033[1;38;5;247m"
    GREY2 = "\033[0m\033[48;5;247m\033[38;5;232m"
    GREY2B = "\033[0m\033[48;5;247m\033[1;38;5;232m"

    LGREY = "\033[0m\033[38;5;250m"
    LGREYB = "\033[0m\033[1;38;5;250m"
    ILGREY = "\033[0m\033[48;5;252m\033[38;5;232m"
    ILGREYB = "\033[0m\033[48;5;252m\033[1;38;5;232m"

    DGREY = "\033[0m\033[38;5;240m"
    DGREYB = "\033[0m\033[1;38;5;240m"

    CYAN = "\033[0m\033[38;5;44m"
    CYANB = "\033[0m\033[1;38;5;44m"

    WHITE = "\033[0m\033[38;5;231m"
    WHITEB = "\033[0m\033[1;38;5;231m"
    WHITE2 = "\033[0m\033[48;5;231m\033[38;5;232m"
    WHITE2B = "\033[0m\033[48;5;231m\033[1;38;5;232m"

    ORANGE = "\033[0m\033[38;5;202m"
    ORANGEB = "\033[0m\033[1;38;5;202m"
    ORANGE2 = "\033[0m\033[38;5;100m"
    ORANGE2B = "\033[0m\033[1;38;5;100m"
    ORANGE3 = "\033[0m\033[38;5;70m"  # Formerly: "CHARTER"
    ORANGE3B = "\033[0m\033[1;38;5;70m"  # Formerly: "CHARTERB"

    IORANGE = "\033[0m\033[48;5;202m\033[38;5;232m"
    IORANGEB = "\033[0m\033[48;5;202m\033[1;38;5;232m"
    IORANGE2 = "\033[0m\033[48;5;100m\033[38;5;232m"
    IORANGE2B = "\033[0m\033[48;5;100m\033[1;38;5;232m"
    IORANGE3 = "\033[0m\033[48;5;70m\033[38;5;232m"  # BEST ORANGE!
    IORANGE3B = "\033[0m\033[48;5;70m\033[1;38;5;232m"  # BEST ORANGE!

    CRED = "\033[0m\033[38;5;203m"  # Red EF3340
    CREDB = "\033[0m\033[1;38;5;203m"  # Red EF3340
    ICRED = "\033[0m\033[38;5;120m\033[48;5;203m"
    ICREDB = "\033[0m\033[1;38;5;120m\033[48;5;203m"

    SRED = "\033[0m\033[38;5;210m"
    SREDB = "\033[0m\033[1;38;5;210m"
    ISRED = "\033[0m\033[38;5;120m\033[48;5;210m"
    ISREDB = "\033[0m\033[1;38;5;120m\033[48;5;210m"

    CORAL = "\033[0m\033[38;5;210m"  # LightCoral #ff8787
    CORALB = "\033[0m\033[1;38;5;210m"  # LightCoral #ff8787
    CORAL2 = "\033[0m\033[38;5;217m"  # LightPink1 #ffafaf
    CORAL2B = "\033[0m\033[1;38;5;217m"  # LightPink1 #ffafaf

    ICORAL = "\033[0m\033[48;5;210m\033[38;5;232m"  # LightCoral #ff8787
    ICORALB = "\033[0m\033[48;5;210m\033[1;38;5;232m"  # LightCoral #ff8787
    ICORAL2 = "\033[0m\033[48;5;217m\033[38;5;232m"  # LightPink1 #ffafaf
    ICORAL2B = "\033[0m\033[48;5;217m\033[1;38;5;232m"  # LightPink1 #ffafaf

    GROTTO = "\033[0m\033[38;5;37m"  # Blue Grotto 059DC0
    GROTTOB = "\033[0m\033[1;38;5;37m"  # Blue Grotto 059DC0
    IGROTTO = "\033[0m\033[48;5;37m\033[38;5;232m"  # Blue Grotto 059DC0
    IGROTTOB = "\033[0m\033[48;5;37m\033[1;38;5;232m"  # Blue Grotto 059DC0

    GOLD = "\033[0m\033[38;5;178m"  # Gold3
    GOLDB = "\033[0m\033[1;38;5;178m"
    GOLD2 = "\033[0m\033[38;5;186m"  # Goldenrod3
    GOLD2B = "\033[0m\033[1;38;5;186m"
    GOLD3 = "\033[0m\033[38;5;220m"  # Goldenrod2
    GOLD3B = "\033[0m\033[1;38;5;220m"

    IGOLD = "\033[0m\033[48;5;178m\033[38;5;232m"  # Gold3
    IGOLDB = "\033[0m\033[48;5;178m\033[1;38;5;232m"
    IGOLD2 = "\033[0m\033[48;5;186m\033[38;5;232m"  # Goldenrod3
    IGOLD2B = "\033[0m\033[48;5;186m\033[1;38;5;232m"
    IGOLD3 = "\033[0m\033[48;5;220m\033[38;5;232m"  # Goldenrod2
    IGOLD3B = "\033[0m\033[48;5;220m\033[1;38;5;232m"

    KHAKI1 = "\033[0m\033[38;5;185m"  # khaki1
    KHAKI1B = "\033[0m\033[1;38;5;185m"  # khakib1
    KHAKI2 = "\033[0m\033[38;5;228m"  # khaki2
    KHAKI2B = "\033[0m\033[1;38;5;228m"  # khakib2
    IKHAKI1 = "\033[0m\033[48;5;185m\033[38;5;232m"  # ikhaki1
    IKHAKI1B = "\033[0m\033[48;5;185m\033[1;38;5;232m"  # ikhakib1
    IKHAKI2 = "\033[0m\033[48;5;228m\033[38;5;232m"  # ikhaki2
    IKHAKI2B = "\033[0m\033[48;5;228m\033[1;38;5;232m"  # ikhakib2

    AQUA1 = "\033[0m\033[38;5;79m"  # aqua1
    AQUA1B = "\033[0m\033[1;38;5;79m"  # aqua2
    IAQUA1 = "\033[0m\033[48;5;79m\033[38;5;232m"  # iaqua1
    IAQUA1B = "\033[0m\033[48;5;79m\033[38;5;232m"  # iaqua1b
    CADET1 = "\033[0m\033[38;5;72m"  # cadet1
    CADET1B = "\033[0m\033[1;38;5;72m"  # cadet2
    ICADET1 = "\033[0m\033[48;5;72m\033[38;5;232m"  # cadet1
    ICADET1B = "\033[0m\033[48;5;72m\033[1;38;5;232m"  # cadet2

    TAN = "\033[0m\033[38;5;180m"
    TANB = "\033[0m\033[1;38;5;180m"
    DESERT = "\033[0m\033[38;5;173m"  # Desert Sun C68B5E
    DESERTB = "\033[0m\033[1;38;5;173m"

    DSKY = "\033[0m\033[38;5;23m"  # DeepSkyBlue4
    DSKYB = "\033[0m\033[1;38;5;23m"
    DSKY2 = "\033[0m\033[38;5;31m"  # DeepSkyBlue3
    DSKY2B = "\033[0m\033[1;38;5;31m"
    DSKY3 = "\033[0m\033[38;5;38m"  # DeepSkyBlue2
    DSKY3B = "\033[0m\033[1;38;5;38m"

    ROYAL = "\033[0m\033[38;5;32m"  # Royal Blue 0087D7
    ROYALB = "\033[0m\033[1;38;5;32m"  # Royal Blue 0087D7

    IDSKY = "\033[0m\033[48;5;23m\033[38;5;231m"
    IDSKYB = "\033[0m\033[48;5;23m\033[1;38;5;231m"
    IDSKY2 = "\033[0m\033[48;5;31m\033[38;5;232m"
    IDSKY2B = "\033[0m\033[48;5;31m\033[1;38;5;232m"
    IDSKY3 = "\033[0m\033[48;5;38m\033[38;5;232m"
    IDSKY3B = "\033[0m\033[48;5;38m\033[1;38;5;232m"

    SKY = "\033[0m\033[38;5;111m"
    SKYB = "\033[0m\033[1;38;5;111m"
    ISKY = "\033[0m\033[48;5;111m\033[38;5;232m"
    ISKYB = "\033[0m\033[48;5;111m\033[1;38;5;232m"
    SKY2 = "\033[0m\033[38;5;153m"
    SKY2B = "\033[0m\033[1;38;5;153m"
    ISKY2 = "\033[0m\033[48;5;153m\033[38;5;232m"
    ISKY2B = "\033[0m\033[48;5;153m\033[1;38;5;232m"

    THISTLE = "\033[0m\033[38;5;182m"
    THISTLEB = "\033[0m\033[1;38;5;182m"
    THISTLE2 = "\033[0m\033[38;5;225m"  # Alt to SKYBLUE
    THISTLE2B = "\033[0m\033[1;38;5;225m"

    CHARTER = "\033[0m\033[38;5;70m"
    CHARTERB = "\033[0m\033[1;38;5;70m"
    CHARTER2 = "\033[0m\033[38;5;112m"
    CHARTER2B = "\033[0m\033[1;38;5;112m"

    STEEL = "\033[0m\033[38;5;67m"  # SteelBlue   #5f87af
    STEELB = "\033[0m\033[1;38;5;67m"
    STEEL2 = "\033[0m\033[38;5;75m"  # SteelBlue1  #5fafff
    STEEL2B = "\033[0m\033[1;38;5;75m"

    SLATE = "\033[0m\033[38;5;61m"
    SLATEB = "\033[0m\033[1;38;5;61m"
    SLATE2 = "\033[0m\033[38;5;105m"  # LightSlateBlue  #8787ff
    SLATE2B = "\033[0m\033[1;38;5;105m"

    SGREEN = "\033[0m\033[38;5;29m"
    SGREENB = "\033[0m\033[1;38;5;29m"
    SGREEN2 = "\033[0m\033[38;5;65m"  # DarkSeaGreen4 #5f875f
    SGREEN2B = "\033[0m\033[1;38;5;65m"
    SGREEN3 = "\033[0m\033[38;5;150m"  # DarkSeaGreen3 #afd787
    SGREEN3B = "\033[0m\033[1;38;5;150m"

    # CUSTOM PRESETS
    WARNING = "\033[0m\033[48;5;112m\033[38;5;232m"
    WARNINGB = "\033[0m\033[48;5;112m\033[1;38;5;232m"
    CAUTION = "\033[0m\033[48;5;34m\033[38;5;232m"
    CAUTIONB = "\033[0m\033[48;5;34m\033[1;38;5;232m"
    CAUTION2 = "\033[0m\033[48;5;202m\033[38;5;231m"
    CAUTION2B = "\033[0m\033[48;5;202m\033[1;38;5;231m"
    ATTENTION = "\033[0m\033[48;5;35m\033[38;5;232m"
    ATTENTIONB = "\033[0m\033[48;5;35m\033[1;38;5;232m"
    ATTENTION2 = "\033[0m\033[38;5;232m\033[48;5;34m"
    ATTENTION2B = "\033[0m\033[1;38;5;232m\033[48;5;34m"
    # ERROR2 = "\033[0m\033[48;5;94m\033[1;38;5;47m"
    # ERROR2B = "\033[0m\033[1;48;5;94m\033[1;38;5;47m"
    ERROR = "\033[0m\033[48;5;240m\033[1;38;5;227m"
    ERRORB = "\033[0m\033[1;48;5;240m\033[1;38;5;227m"
    ERROR1 = "\033[0m\033[48;5;240m\033[1;38;5;153m"
    ERROR1B = "\033[0m\033[1;48;5;240m\033[1;38;5;153m"
    ERROR2 = "\033[0m\033[48;5;196m\033[38;5;232m"
    ERROR2B = "\033[0m\033[48;5;196m\033[1;38;5;232m"

    INFO = "\033[0m\033[48;5;223m\033[38;5;232m"  # NavajoWhite1
    INFOB = "\033[0m\033[48;5;223m\033[1;38;5;232m"  # NavajoWhite1
    INFO1 = "\033[0m\033[48;5;120m\033[38;5;232m"  # NavajoWhite1
    INFO1B = "\033[0m\033[48;5;120m\033[1;38;5;232m"  # NavajoWhite1
    INFO2 = "\033[0m\033[48;5;173m\033[38;5;232m"  # desert
    INFO2B = "\033[0m\033[48;5;173m\033[1;38;5;232m"  # desertb
    INFO3 = "\033[0m\033[48;5;153m\033[38;5;232m"  # sky2
    INFO3B = "\033[0m\033[48;5;153m\033[1;38;5;232m"  # sky2b
    INFO4 = "\033[0m\033[48;5;188m\033[38;5;232m"  # grey84
    INFO4B = "\033[0m\033[48;5;188m\033[1;38;5;232m"  # grey84

    TITLE = "\033[0m\033[97m\033[48;5;91m"
    TITLEB = "\033[0m\033[1;97m\033[48;5;91m"
    GREY84 = "\033[0m\033[38;5;188m"  # grey84
    GREY84B = "\033[0m\033[1;38;5;188m"  # grey84b

    # FONT STYLES
    STANDARD = "\033[0m"
    STANDARDB = "\033[1;0m"
    BOLD = "\033[1m"
    BOLDB = "\033[1;1m"
    NORMAL = "\033[0m\033[38;5;8m"
    NORMALB = "\033[0m\033[1;38;5;8m"
    ITALIC = "\033[3m"
    ITALICB = "\033[1;3m"
    UNDERLINE = "\033[4m"
    UNDERLINEB = "\033[1;4m"
    BLINK = "\033[5m"
    BLINKB = "\033[1;5m"
    INVERT = "\033[7m"
    INVERTB = "\033[1;7m"
    STRIKE = "\033[9m"
    STRIKEB = "\033[1;9m"
    END = "\033[0m"
    OFF = "\033[0m"

    # Monochrome Color Set:
    RAVE = "\033[0m\033[38;5;181m"  # Mauve D3B1C2
    RAVEB = "\033[0m\033[1;38;5;181m"  # Mauve D3B1C2
    IRAVE = "\033[0m\033[48;5;181m\033[38;5;232m"  # Mauve D3B1C2
    IRAVEB = "\033[0m\033[1;48;5;181m\033[1;38;5;232m"  # Mauve D3B1C2
    IVORY = "\033[0m\033[38;5;152m"  # Ivory EDE4E3
    IVORYB = "\033[0m\033[1;38;5;152m"  # Ivory EDE4E3
    NAVY = "\033[0m\033[38;5;23m"  # Navy Blue 1E3D58
    NAVYB = "\033[0m\033[1;38;5;23m"  # Navy Blue 1E3D58
    TAUPE = "\033[0m\033[38;5;138m"  # Rosy Brown #af8787
    TAUPEB = "\033[0m\033[1;38;5;138m"  # Rosy Brown #af8787

    LAVA = "\033[0m\033[38;5;223m"  # NavajoWhite1
    LAVAB = "\033[0m\033[1;38;5;223m"  # NavajoWhite1

    ILAVA = "\033[0m\033[48;5;223m\033[38;5;232m"  # NavajoWhite1
    ILAVAB = "\033[0m\033[48;5;223m\033[1;38;5;232m"  # NavajoWhite1

    CREAM = "\033[0m\033[38;5;230m"  # Cornsilk1 #ffffd7
    CREAMB = "\033[0m\033[1;38;5;230m"  # Cornsilk1 #ffffd7

    ICREAM = "\033[0m\033[48;5;230m\033[38;5;232m"  # Cornsilk1 #ffffd7
    ICREAMB = "\033[0m\033[48;5;230m\033[1;38;5;232m"  # Cornsilk1 #ffffd7

    # https://www.oberlo.com/blog/color-combinations-cheat-sheet
    # https://www.ditig.com/256-colors-cheat-sheet


class CustomFormatter(Formatter):
    grey: str = "\x1b[38;20m"
    yellow: str = "\x1b[33;20m"
    red: str = "\x1b[31;20m"
    bold_red: str = "\x1b[31;1m"
    reset: str = "\x1b[0m"
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"

    FORMATS: Dict[int, str] = {
        logging.DEBUG: f"{grey}{format}{reset}",
        logging.INFO: f"{grey}{format}{reset}",
        logging.WARNING: f"{yellow}{format}{reset}",
        logging.CRITICAL: f"{red}{format}{reset}",
        logging.CRITICAL: f"{bold_red}{format}{reset}",
    }

    def format(self, record: LogRecord) -> str:
        log_fmt: str | None = self.FORMATS.get(record.levelno)
        formatter: Formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


class space:
    p0 = ""
    p1 = " " * 1
    p2 = " " * 2
    p3 = " " * 3
    p4 = " " * 4
    p5 = " " * 5
    p6 = " " * 6
    p7 = " " * 7
    p8 = " " * 8
    p9 = " " * 9
    p10 = " " * 10
    p20 = " " * 20
    p30 = " " * 30
    p40 = " " * 40
    p50 = " " * 50


class newline:
    l1 = r"\n"
    l2 = r"\n\n"
    l3 = r"\n\n\n"
    l4 = r"\n\n\n\n"
