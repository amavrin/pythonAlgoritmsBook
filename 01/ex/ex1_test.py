import pytest
import ex1


@pytest.fixture(scope="module")
def test_data() -> list:
    data = []
    data.append("арозаупаланалапуазора")
    return data


NOT_PALINDROME="abcdefg"


def test_is_palindrome1(test_data):
    for data in test_data:
        assert ex1.is_palindrome1(data)
        assert not ex1.is_palindrome1(NOT_PALINDROME)


def test_is_palindrome2(test_data):
    for data in test_data:
        assert ex1.is_palindrome2(data)
        assert not ex1.is_palindrome2(NOT_PALINDROME)