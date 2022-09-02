import argparse

parser = argparse.ArgumentParser(description='Bandwidth test')
parser.add_argument(
    '-s', '--service',
    required=True,
    type=int,
    nargs='?',
    help='Service ID for which the pattern list will be downloaded',
)
