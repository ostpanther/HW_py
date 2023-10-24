from argparse import ArgumentParser

from .download_html import download_html
from .html_to_txt import html_to_txt
from .paths import show_paths

commands = {
    "show_paths": show_paths,
    "download_html": download_html,
    "html_to_txt": html_to_txt,
}
usage_help = "python -m scripts <command>"

parser = ArgumentParser(usage=usage_help)
parser.add_argument("command", choices=set(commands))
args = parser.parse_args()

commands[args.command]()
