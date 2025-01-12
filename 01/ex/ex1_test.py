import pytest
import ex1


@pytest.fixture(scope="module")
def test_data() -> list:
    data = ["арозаупаланалапуазора"]
    return data


NOT_PALINDROME="abcdefg"


def test_is_palindrome1(test_data):
    for data in test_data:
        assert ex1.is_palindrome1(data), f"Expected {data} to be a palindrome"
    assert not ex1.is_palindrome1(NOT_PALINDROME), f"Expected {NOT_PALINDROME} to not be a palindrome"


def test_is_palindrome2(test_data):
    for data in test_data:
        assert ex1.is_palindrome2(data), f"Expected {data} to be a palindrome"
    assert not ex1.is_palindrome2(NOT_PALINDROME), f"Expected {NOT_PALINDROME} to not be a palindrome"


def test_is_palindrome3(test_data):
    for data in test_data:
        assert ex1.is_palindrome3(data), f"Expected {data} to be a palindrome"
    assert not ex1.is_palindrome3(NOT_PALINDROME), f"Expected {NOT_PALINDROME} to not be a palindrome"