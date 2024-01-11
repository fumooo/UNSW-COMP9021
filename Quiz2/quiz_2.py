# Written by *** for COMP9021
#
# Prompts the user for the integers 0, 1... n, input
# in some order, for some natural number n,
# making up a list your_list,
# and for two integers, the second of which, say p,
# is between 0 and 10, to create a permutation of
# {0, ... p-1}, say my_list.
#
# Removes from your_list what is currently the smallest
# or largest element if it is curently the first or last
# element of the list, for as long as it can be done.
#
# Displays a picture that represents how to travel from
# 0 to p-1 in my_list, based on where they are located
# in the list.


from random import seed, shuffle
import sys


try: 
    your_list = [int(x) for x in
                     input('Enter a permutation of 0, ..., n '
                           'for some n >= 0: '
                          ).split()
                ]
    if not your_list:
        raise ValueError
    your_list_as_set = set(your_list)
    if len(your_list_as_set) != len(your_list)\
       or your_list_as_set != set(range(len(your_list))):
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try: 
    for_seed, length =\
        (int(x) for x in input('Enter two integers, '
                               'the second one between 0 and 10: '
                              ).split()
        )
    print(for_seed,length)
    if not 0 <= length <= 10:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
my_list = list(range(length))
shuffle(my_list)
print('Here is your list:')
print('  ', your_list)
print('Here is my list:')
print('  ', my_list)

# INSERT THE FIRST PART OF YOUR CODE HERE

print()
print('Removing again and again the currently largest\n'
      'or smallest element in your list for as long as\n'
      'it currently starts or ends the list, we get:'
     )
print(your_list)
print()
print("That's how to travel in my list:")

# INSERT THE SECOND PART OF YOUR CODE HERE
