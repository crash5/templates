import argparse
import logging

from {{ cookiecutter.package_name }}.add_numbers import add_numbers
import {{ cookiecutter.package_name }}.version as ver


logger = logging.getLogger(__name__)


def main():
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

    logger.info(f"The two numbers are {a} and {b}")
    print(add_numbers(a, b))


def setup_logger():
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)

    lf = logging.Formatter(
        fmt="%(asctime)s [%(levelname)-8s] %(message)s [logger=%(name)s process_id=%(process)d file=%(filename)s line=%(lineno)d]"
    )

    sh = logging.StreamHandler()
    sh.setLevel(logging.DEBUG)
    sh.setFormatter(lf)
    root_logger.addHandler(sh)

    # fh = logging.FileHandler("log.txt")
    # fh.setLevel(logging.DEBUG)
    # fh.setFormatter(lf)
    # root_logger.addHandler(fh)


if __name__ == "__main__":
    setup_logger()
    main()
