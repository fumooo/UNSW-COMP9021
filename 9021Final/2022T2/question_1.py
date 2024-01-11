# A sequence of identical digits is collapsed to one digit
# in the returned integer.
#
# You can assume that the function is called with an integer
# as argument.


def collapse(number):
    '''
    >>> collapse(0)
    0
    >>> collapse(-0)
    0
    >>> collapse(9)
    9
    >>> collapse(-9)
    -9
    >>> collapse(12321)
    12321
    >>> collapse(-12321)
    -12321
    >>> collapse(-1111222232222111)
    -12321
    >>> collapse(1155523335551116111666)
    152351616
    >>> collapse(-900111212777394440300)
    -9012127394030
    '''
    return 0
    # REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE

if __name__ == '__main__':
    import doctest
    doctest.testmod()
