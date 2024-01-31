import argparse
import logging

from {{ cookiecutter.package_name }}.add_numbers import add_numbers
import {{ cookiecutter.package_name }}.version as ver


logger = logging.getLogger(__name__)


def main(a, b):
    logger.info(f"The two numbers are {a} and {b}")
    print(add_numbers(a, b))


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format="[%(asctime)s][%(process)6d] %(levelname)8s: %(message)s [%(name)s]")

    version = ver.version_string()
    logger.info(f"{{ cookiecutter.package_name }} version: v{version}")

    parser = argparse.ArgumentParser(prog="{{ cookiecutter.package_name }}", description="{{ cookiecutter.project_short_description }}")
    parser.add_argument(
        "-v", "--version",
        action="version",
        version=f"%(prog)s v{version}"
    )

    parser.add_argument("integers", metavar="N", type=int, nargs=2, help="Two numbers to sum.")
    args = parser.parse_args()

    a = args.integers[0]
    b = args.integers[1]

    main(a, b)
