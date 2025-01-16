import random
import timeit
from prettytable import PrettyTable

from algs.counting import RecordedItem
from ch01.challenge import partition, linear_median


def other_median(a: list):
    a = sorted(a)
    return a[len(a)//2-1]


def run_linear_median(l: list, print_stat: bool = False):
    RecordedItem.clear()
    res: RecordedItem = linear_median(l)
    if print_stat: print(RecordedItem.report())
    return res.val


def run_other_median(l: list, print_stat: bool = False):
    RecordedItem.clear()
    res: RecordedItem = other_median(l)
    if print_stat: (RecordedItem.report())
    return res.val


def main():
    l = list(range(10))
    random.shuffle(l)
    l_recorded = [RecordedItem(i) for i in l]

    counts = []
    times_linear = []
    times_other = []

    for i in range(4, 7):
        lst = l_recorded.copy()
        counts.append(10**i)

        t_linear = timeit.timeit(lambda: run_linear_median(lst), number=10**i)
        times_linear.append(round(t_linear.real, ndigits=3))

        t_other = timeit.timeit(lambda: run_other_median(lst), number=10**i)
        times_other.append(round(t_other.real, ndigits=3))

    table = PrettyTable()
    table.add_column(fieldname="Count", column=counts)
    table.add_column(fieldname="linear", column=times_linear)
    table.add_column(fieldname="other", column=times_other)

    print(table)







if __name__ == "__main__":
    main()