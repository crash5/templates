from {{ cookiecutter.package_name }}.add_numbers import add_numbers


def test_must_fail():
    assert add_numbers(3, 2) == 6


def test_must_pass():
    assert add_numbers(3, 3) == 6
