import argparse
import logging

from .add_numbers import add_numbers


logger = logging.getLogger(__name__)


def main(a, b):
    logger.info(f'The two numbers are {a} and {b}')
    print(add_numbers(a, b))


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    parser = argparse.ArgumentParser(prog='{{ cookiecutter.package_name }}', description='Add two numbers easily.')
    parser.add_argument('integers', metavar='N', type=int, nargs=2, help='Two numbers to sum.')
    args = parser.parse_args()

    a = args.integers[0]
    b = args.integers[1]

    main(a, b)
