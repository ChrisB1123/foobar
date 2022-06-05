from math import factorial as fact
from fractions import gcd
from collections import Counter


# find the conjugacy size of an unordered integer partition
def conjugacy_size(partition):
    n = sum(partition)
    terms = Counter(partition)
    denom = 1
    for k, v in terms.iteritems():
        denom *= pow(k, v) * fact(v)

    return fact(n)/denom


def int_partition(n):
    return list(int_partition_yield(n))


# efficient algorithm for calculating the different integer partitions for a given n
def int_partition_yield(n):
    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2 * x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            yield tuple(a[: k + 2])
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        yield tuple(a[: k + 1])


def solution(w, h, s):

    mod_g = fact(w) * fact(h)

    # the different types of permutations of interchanging rows and columns are defined
    # by the integer partitions for n = h or n = w respectively
    row_permutations = int_partition(h)
    col_permutations = int_partition(w)

    summation = 0

    # for each row integer partition, for each of column integer partition, use the elements of the partitions to find
    # the exponent for each term
    for i in row_permutations:
        for j in col_permutations:
            counter = 0
            for a in i:
                for b in j:
                    # sum to find exponent
                    counter += gcd(a, b)

            symmetry_factor = conjugacy_size(i)*conjugacy_size(j)
            summation += symmetry_factor*pow(s, counter)

    return str(summation/mod_g)


if __name__ == '__main__':
    print 'solution 1 (7):', solution(2, 2, 2)
    print 'solution 2 (430):', solution(2, 3, 4)
    print 'solution 3 (??):', solution(12, 12, 20)