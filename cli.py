import argparse


def cli_args():

    # Create the argument parser and add the ability to take arguments
    parser = argparse.ArgumentParser(
        prog='checker', description='Checks connectivity of URLs'
    )

    parser.add_argument(
        '-u',
        '--urls',
        metavar='URLs',
        nargs="+",
        type=str,
        default=[]
        help='Enter one or multiple URLs to check their availability!'
    )
    # Return Namespace
    return parser.parse_args()


def checker_result(result, url, error=''):

    # Display results

    print(f'{url} ')
    if result:
        print("has connectivity!")
    else:
        print(f"is offline or down :(  ERROR: {error}")
