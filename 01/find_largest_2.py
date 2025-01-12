import random


def largest(arr, not_more_than=None):
    maximum = arr[0]
    for e in arr[1:]:
        if e <= maximum:
            continue
        if not_more_than is not None and e >= not_more_than:
            continue
        maximum = e
    return maximum


def largest2(arr):
    max1 = largest(arr)
    max2 = largest(arr, max1)
    return max1, max2


def largest2bymax(arr):
    s_arr = sorted(arr, reverse=True)
    return (s_arr[0], s_arr[1])


def largest2x(arr):
    first, second = arr[:2]
    if second > first:
        first, second = second, first
    for elem in arr[2:]:
        if elem > first:
            first, second = elem, first
            continue
        if elem > second:
            second = elem
    return first, second



def main():
    lst = list(range(100))
    random.shuffle(lst)
    print(largest(lst))
    print(largest2(lst))
    print(largest2bymax(lst))


if __name__ == "__main__":
    main()