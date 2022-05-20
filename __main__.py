from pydoc import cli
from checker import online
from cli import cli_args
import sys


def main():

    # Run the checker
    user_args = cli_args()
    urls = online(user_args)
    if not urls:
        print("No URL found", file=sys.stderr)
        sys.exit(1)
    _synchronous_check(urls)
