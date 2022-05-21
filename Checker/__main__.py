from checker import is_online
from cli import cli_args, checker_result
import pathlib
import sys


def main():

    # Run the checker
    user_args = cli_args()
    urls = _get_urls(user_args)
    if not urls:
        print("No URL found", file=sys.stderr)
        sys.exit(1)
    _synchronous_check(urls)


def _get_urls(user_args):

    # Returns a list of URLs from command line and/or a file.
    urls = user_args.urls
    if user_args.input_file:
        urls += _read_urls_from_file(user_args.input_file)
    return urls


def _read_urls_from_file(file):

    # Reads URLs from file and stores it to list.
    file_path = pathlib.Path(file)
    if file_path.is_file():
        with file_path.open() as urls_file:
            urls = [url.strip() for url in urls_file]
            if urls:
                return urls
            print(f"Error: empty input file, {file}", file=sys.stderr)
    else:
        print("Error: input file not found", file=sys.stderr)
    return []


def _synchronous_check(urls):
    for url in urls:
        error = ""
        try:
            result = is_online(url)
        except Exception as e:
            result = False
            error = str(e)
        checker_result(result, url, error)


if __name__ == "__main__":
    main()