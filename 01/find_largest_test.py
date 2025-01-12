from find_largest_2 import largest, largest2bymax, largest2, largest2x
import random


def test_largest():
    lst = list(range(100))
    random.shuffle(lst)
    assert largest(lst) == 99


def test_largest2():
    lst = list(range(100))
    random.shuffle(lst)
    assert largest2(lst) == (99, 98)


def test_largest2bymax():
    lst = list(range(100))
    random.shuffle(lst)
    assert largest2bymax(lst) == (99, 98)


def test_largest2x():
    lst = list(range(100))
    random.shuffle(lst)
    assert largest2x(lst) == (99, 98)