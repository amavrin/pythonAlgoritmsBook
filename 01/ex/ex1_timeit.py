import timeit
import ex1
from prettytable import PrettyTable


PALINDROME="dennisandednasinned"


def run_palindrome1():
    ex1.is_palindrome1(PALINDROME)

def run_palindrome2():
    ex1.is_palindrome2(PALINDROME)

def measure():
    counts = []
    times1 = []
    times2 = []
    for k in range(8, 21, 4):
        counts.append(k)
        t1 = timeit.timeit(run_palindrome1, number=2**k)
        t2 = timeit.timeit(run_palindrome2, number=2**k)
        times1.append(round(t1.real, ndigits=3))
        times2.append(round(t2.real, ndigits=3))

    table = PrettyTable()
    table.add_column("Count 2**N", column=counts)
    table.add_column("Palindrome1", column=times1)
    table.add_column("Palindrome2", column=times2)
    print(table)

def main():
    measure()


if __name__ == "__main__":
    main()