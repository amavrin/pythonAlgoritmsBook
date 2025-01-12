import pytest

from find_largest_2 import largest, largest2bymax, largest2, largest2x
import random


REPEAT = 10


@pytest.fixture(scope="module")
def prepare_list() -> list:
    lst = list(range(100))
    ret = []
    for i in range(REPEAT):
        random.shuffle(lst)
        ret.append(list(lst))
    return ret


@pytest.mark.parametrize("i", range(REPEAT))
def test_largest(prepare_list, i: int):
    assert largest(prepare_list[i]) == 99


@pytest.mark.parametrize("i", range(REPEAT))
def test_largest2(prepare_list, i: int):
    assert largest2(prepare_list[i]) == (99, 98)


@pytest.mark.parametrize("i", range(REPEAT))
def test_largest2bymax(prepare_list, i: int):
    assert largest2bymax(prepare_list[i]) == (99, 98)


@pytest.mark.parametrize("i", range(REPEAT))
def test_largest2x(prepare_list, i: int):
    assert largest2x(prepare_list[i]) == (99, 98)