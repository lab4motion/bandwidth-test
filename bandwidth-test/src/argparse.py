import argparse

parser = argparse.ArgumentParser(description='Bandwidth test')
parser.add_argument(
    '-s', '--service',
    required=True,
    type=int,
    nargs='?',
    help='Service ID for which the pattern list will be downloaded',
)
parser.add_argument(
    '-o', '--optimize',
    required=False,
    action='store_true',
    help=(
        'Use for decreasing the size of downloaded thumbnails: '
        'max 700px and 50%% of quality.'
    ),
)
