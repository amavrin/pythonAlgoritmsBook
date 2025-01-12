import timeit
import ex1
from prettytable import PrettyTable


# PALINDROME="dennisandednasinned"
PALINDROME = "a" * 100
NOT_PALINDROME = "a" * 100 + "b"


def run_palindrome1():
    ex1.is_palindrome1(PALINDROME)
    ex1.is_palindrome1(NOT_PALINDROME)


def run_palindrome2():
    ex1.is_palindrome2(PALINDROME)
    ex1.is_palindrome2(NOT_PALINDROME)


def run_palindrome3():
    ex1.is_palindrome3(PALINDROME)
    ex1.is_palindrome3(NOT_PALINDROME)


def run_palindrome4():
    ex1.is_palindrome4(PALINDROME)
    ex1.is_palindrome4(NOT_PALINDROME)


def measure():
    counts = []
    times1 = []
    times2 = []
    times3 = []
    times4 = []
    for k in range(8, 17, 4):
        counts.append(k)
        t1 = timeit.timeit(run_palindrome1, number=2**k)
        t2 = timeit.timeit(run_palindrome2, number=2**k)
        t3 = timeit.timeit(run_palindrome3, number=2**k)
        t4 = timeit.timeit(run_palindrome4, number=2**k)
        times1.append(round(t1.real, ndigits=3))
        times2.append(round(t2.real, ndigits=3))
        times3.append(round(t3.real, ndigits=3))
        times4.append(round(t4.real, ndigits=3))

    table = PrettyTable()
    table.add_column("Count 2**N", column=counts)
    table.add_column("Palindrome1", column=times1)
    table.add_column("Palindrome2", column=times2)
    table.add_column("Palindrome3", column=times3)
    table.add_column("Palindrome4", column=times4)
    print(table)


def main():
    measure()


if __name__ == "__main__":
    main()