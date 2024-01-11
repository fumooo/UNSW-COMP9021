## Written by *** for COMP9021

# Implements a function that computes the maximum
# number of primes within a window of a given size,
# the first of which starts from a given lower bound
# and the last of which ends at a given upper bound.
# For all windows that achieve that maximum number
# within the window; outputs those two primes
# from smallest to largest first primes.

from math import sqrt


def sieve_of_primes_up_to(n):  # IS primes
    sieve = [True] * (n + 1)
    for p in range(2, round(sqrt(n)) + 1):
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return sieve


# You can assume that the function will be called with
# size a strictly positive integer,
# lower_bound an integer at least equal to 2, and
# upper_bound an integer at least equal to lower_bound.
# The function won't be tested for values of upper_bound
# greater than 10,000,000.
def primes_in_window(size, lower_bound, upper_bound):
    if size > upper_bound - lower_bound + 1:
        print('Window size is too large for these bounds,',
              'leaving it there.'
              )
        return
    # INSERT YOUR CODE HERE

    if size <= 0:
        print("size is a strictly positive integer")
        return
    sieve = sieve_of_primes_up_to(upper_bound)
    # print(sieve)

    #     print("There are at most 3 primes in a window of size " + str(size) + '.')



    LargestNum = 0
    List = []
    #roof begin
    for i in range(lower_bound, upper_bound + 1):
        MesDic = {"start_P": 0, "end_P": 0, "largest_P": 0, "Number": 0}
        start_P = i
        end_P = i + size - 1
        largest_P = 0 #the largest point
        Number = 0 # the sum of the prime
        if(end_P > upper_bound):
            break

        #begin
        if(sieve[start_P] == True and size == 1):
            largest_P = start_P
            MesDic["start_P"] = start_P
            MesDic["end_P"] = end_P
            MesDic["largest_P"] = largest_P
            MesDic["Number"] = Number
            LargestNum = Number
            # print(MesDic)
            List.append(MesDic)


        if(sieve[start_P] == True and size > 1):
            for m in range(start_P, end_P + 1):
                if(sieve[m] == True):
                    Number = Number + 1 #the sum of prime +1
                    largest_P = m
            if(Number != 1):#if prime existing
                MesDic["start_P"] = start_P
                MesDic["end_P"] = end_P
                MesDic["largest_P"] = largest_P
                MesDic["Number"] = Number
                List.append(MesDic)
            if(LargestNum < Number):
                LargestNum = Number
        else:
            continue

    #Output
    # print(List)
    # print(LargestNum)
    if(len(List) == 0):
        print("There is no prime in a window of size " + str(size)+ ".")
    if(len(List) != 0 and size == 1):
        print("There is at most one prime in a window of size " + str(size)+ ".")
        for i in List:
            if(i["Number"] == LargestNum):
                print("In some window, the smallest prime is " + str(i["start_P"]) + " and the largest one is " + str(i["largest_P"]) + ".")
    if(len(List) != 0 and size >1 ):
        print("There are at most " + str(LargestNum) + " primes in a window of size " + str(size) + ".")
        for i in List:
            if(i["Number"] == LargestNum):
                print("In some window, the smallest prime is " + str(i["start_P"]) + " and the largest one is " + str(i["largest_P"]) + ".")
        # print(start_P,end_P)

primes_in_window(1000, 1000, 1000000)


