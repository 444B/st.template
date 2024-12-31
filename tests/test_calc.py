import pytest
from sttemplate import add_numbers


def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0.1, 0.2) == pytest.approx(0.3)
    assert add_numbers(-2.5, 3.7) == pytest.approx(1.2)
