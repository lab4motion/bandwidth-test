import argparse

parser = argparse.ArgumentParser(
    description='Decrease the size of products and patterns',
)
parser.add_argument(
    '-c', '--customer',
    required=True,
    type=int,
    nargs='?',
    help='Customer ID for which the products and patterns will be decreased',
)
