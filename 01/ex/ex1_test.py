import pytest
import ex1


@pytest.fixture(scope="module")
def test_simple_data() -> list:
    data = ["арозаупаланалапуазора"]
    return data


@pytest.fixture(scope="module")
def test_complex_data() -> list:
    data = ["А роза упала на лапу Азора!"]
    return data


NOT_PALINDROME="abcdefg"


def test_is_palindrome1(test_simple_data):
    for data in test_simple_data:
        assert ex1.is_palindrome1(data), f"Expected {data} to be a palindrome"
    assert not ex1.is_palindrome1(NOT_PALINDROME), f"Expected {NOT_PALINDROME} to not be a palindrome"


def test_is_palindrome2(test_simple_data):
    for data in test_simple_data:
        assert ex1.is_palindrome2(data), f"Expected {data} to be a palindrome"
    assert not ex1.is_palindrome2(NOT_PALINDROME), f"Expected {NOT_PALINDROME} to not be a palindrome"


def test_is_palindrome3(test_simple_data):
    for data in test_simple_data:
        assert ex1.is_palindrome3(data), f"Expected {data} to be a palindrome"
    assert not ex1.is_palindrome3(NOT_PALINDROME), f"Expected {NOT_PALINDROME} to not be a palindrome"


def test_is_palindrome4(test_simple_data, test_complex_data):
    for data in test_simple_data:
        assert ex1.is_palindrome4(data), f"Expected {data} to be a palindrome"
    for data in test_complex_data:
        assert ex1.is_palindrome4(data), f"Expected {data} to be a palindrome"
    assert not ex1.is_palindrome4(NOT_PALINDROME), f"Expected {NOT_PALINDROME} to not be a palindrome"