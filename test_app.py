"""Unit tests"""

from app import add_numbers

def test_add_numbers():
    """Make sure that it all adds up"""

    assert add_numbers(5, 8) == 13
