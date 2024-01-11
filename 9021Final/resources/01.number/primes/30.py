'''
Will be tested with a at equal equal to 2 and b at most equal to 10_000_000.
'''

import sys
from math import sqrt
from itertools import compress


def f(a, b):
    '''
    >>> f(2, 2)
    There is a unique prime number beween 2 and 2.
    >>> f(2, 3)
    There are 2 prime numbers between 2 and 3.
    >>> f(2, 5)
    There are 3 prime numbers between 2 and 5.
    >>> f(4, 4)
    There is no prime number beween 4 and 4.
    >>> f(14, 16)
    There is no prime number beween 14 and 16.
    >>> f(3, 20)
    There are 7 prime numbers between 3 and 20.
    >>> f(100, 800)
    There are 114 prime numbers between 100 and 800.
    >>> f(123, 456789)
    There are 38194 prime numbers between 123 and 456789.
    >>> f(24, 78)
    There are 12 prime numbers between 24 and 78.
    >>> f(11, 56)
    There are 12 prime numbers between 11 and 56.
    >>> f(23, 534)
    There are 91 prime numbers between 23 and 534.
    >>> f(34, 3463)
    There are 474 prime numbers between 34 and 3463.
    >>> f(143, 342)
    There are 34 prime numbers between 143 and 342.
    >>> f(234, 457)
    There are 37 prime numbers between 234 and 457.
    >>> f(1000, 3434)
    There are 313 prime numbers between 1000 and 3434.
    >>> f(8933, 23414)
    There are 1497 prime numbers between 8933 and 23414.
    >>> f(2342, 235235)
    There are 20505 prime numbers between 2342 and 235235.
    >>> f(235, 3423524)
    There are 245064 prime numbers between 235 and 3423524.
    >>> f(9984, 232454)
    There are 19404 prime numbers between 9984 and 232454.
    >>> f(234554, 3423523)
    There are 224321 prime numbers between 234554 and 3423523.
    >>> f(909812, 2312414)
    There are 98351 prime numbers between 909812 and 2312414.
    >>> f(324235, 3253463)
    There are 205866 prime numbers between 324235 and 3253463.
    >>> f(3, 3125563)
    There are 225208 prime numbers between 3 and 3125563.
    >>> f(555, 5555555)
    There are 384225 prime numbers between 555 and 5555555.
    >>> f(32423, 456346)
    There are 34706 prime numbers between 32423 and 456346.
    >>> f(1, 1232553)
    There are 95234 prime numbers between 1 and 1232553.
    >>> f(9834, 435546)
    There are 35394 prime numbers between 9834 and 435546.
    >>> f(23, 4461224)
    There are 313395 prime numbers between 23 and 4461224.
    >>> f(234235, 5645747)
    There are 369351 prime numbers between 234235 and 5645747.
    >>> f(145667, 7834134)
    There are 515821 prime numbers between 145667 and 7834134.
    >>> f(672342, 9341232)
    There are 569234 prime numbers between 672342 and 9341232.
    >>> f(7823045, 9079934)
    There are 78780 prime numbers between 7823045 and 9079934.
    >>> f(13, 9998734)
    There are 664503 prime numbers between 13 and 9998734.
    '''
    number_of_primes_at_most_equal_to_b = 0
    # Insert your code here


if __name__ == '__main__':
    import doctest
    doctest.testmod()
