from pathlib import Path

from colorist import Color

_THIS_FILE = Path(__file__)
SCRIPTS_DIR = _THIS_FILE.parent
ROOT_DIR = SCRIPTS_DIR.parent
HTML_DIR = ROOT_DIR / "html"
TXT_DIR = ROOT_DIR / "txt"


def show_paths() -> None:
    """Распечатать пути к подпапкам проекта."""
    print(f"Project root: {Color.BLUE}'{ROOT_DIR}'{Color.OFF}")
    print(f"* scripts:    {Color.BLUE}'{SCRIPTS_DIR}'{Color.OFF}")
    print(f"* html:       {Color.BLUE}'{HTML_DIR}'{Color.OFF}")
    print(f"* texts:      {Color.BLUE}'{TXT_DIR}'{Color.OFF}")
