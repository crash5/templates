import argparse
import logging
import datetime
from pathlib import Path
import sys
from typing import Optional, Union

from {{ cookiecutter.package_name }}.add_numbers import add_numbers
import {{ cookiecutter.package_name }}.version as ver


logger = logging.getLogger(__name__)


def handle_command_line() -> None:
    setup_logger("./log")

    version = ver.version_string()
    logger.info(f"{{ cookiecutter.package_name }} version: v{version}")

    parser = argparse.ArgumentParser(prog="{{ cookiecutter.package_name }}", description="{{ cookiecutter.project_short_description }}")
    parser.add_argument(
        "-v", "--version",
        action="version",
        version=f"%(prog)s v{version}"
    )

    parser.add_argument("integers", metavar="N", type=int, nargs=2, help="Two numbers to sum.")

    # parser.add_argument(
    #     "-j",
    #     "--jsonConfig",
    #     required=False,
    #     help="Path to the configuration file or folder. Folder must contain exactly one JSON file.",
    #     type=Path,
    # )
    #
    args = parser.parse_args()

    a = args.integers[0]
    b = args.integers[1]

    try:
        logger.info(f"The two numbers are {a} and {b}")
        print(add_numbers(a, b))
    except Exception as e:
        logger.exception(e)


def setup_logger(file_path: Optional[Union[str, Path]] = None) -> None:
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)

    lf = logging.Formatter(
        fmt="%(asctime)s [%(levelname)-8s] %(message)s [logger=%(name)s process_id=%(process)d file=%(filename)s line=%(lineno)d]"
    )
    # lf.converter = time.gmtime  # for UTC time

    sh_out = logging.StreamHandler(sys.stdout)
    sh_out.setLevel(logging.DEBUG)
    sh_out.setFormatter(lf)
    root_logger.addHandler(sh_out)

    sh_err = logging.StreamHandler(sys.stderr)
    sh_err.setLevel(logging.WARNING)
    sh_err.setFormatter(lf)
    root_logger.addHandler(sh_err)

    if file_path and Path(file_path).is_dir():
        date_for_log = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        fh = logging.FileHandler(f"{file_path}/{date_for_log}.log")
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(lf)
        root_logger.addHandler(fh)


if __name__ == "__main__":
    handle_command_line()
