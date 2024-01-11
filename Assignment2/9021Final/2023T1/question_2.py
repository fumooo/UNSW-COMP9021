# Given a dictionary D and a key x, there is a (unique) loop
# containing x if there are keys x_1, ..., x_k such that:
# D maps x to x_1
# D maps x_1 to x_2
# ...
# D maps x_{k-1} to x_k
# x_1, ..., x_{k-1} are all different to x and x_k is x
# (in the particular case where k = 1, D maps x to x).
#
# When the loop does not exist, the function prints out nothing.
# When the loop exists, the function prints out the loop,
# STARTING AND ENDING with the SMALLEST element in the loop.
#
# You can assume that the function is called with as first argument,
# a dictionary having nothing but integers as keys and values,
# and with as second argument, an integer.

# {1: 2, 2: 2}
def check_cycle(D, x):
    result = None
    if x in D:
        cycle = [x]
        # 如果cycle的最后一个在字典里面
        while cycle[-1] in D:
            value = D[cycle[-1]]
            # 从头到尾循环一遍了
            if value == cycle[0]:
                # 找到了我们想要的结果
                cycle.append(value)
                result = cycle
                break
            elif value in cycle:
                # 直接跳出
                break
            cycle.append(value)
    return result


def loop(D, x):
    '''
    # >>> loop({1: 1}, 0)
    # >>> loop({1: 2, 2: 2}, 1)
    # >>> loop({1: 2, 2: 3}, 1)
    # >>> loop({1: 2, 2: 3, 3: 2}, 1)
    # >>> loop({1: 1}, 1)
    # 1--1
    # >>> loop({1: 2, 2: 1}, 2)
    # 1--2--1
    # >>> loop({12: 14, 13: 14, 14: 7, 7: 12, 6: 8, 8: 6, 5: 11}, 14)
    # 7--12--14--7
    # >>> loop({0: 4, 1: 0, 2: 1, 3: 2, 4: 7, 5: 6, 6: 4, 7: 0, 8: 8, 9: 4}, 4)
    # 0--4--7--0
    # >>> loop({0: 7, 1: 7, 2: 3, 3: 8, 4: 6, 5: 8, 6: 6, 7: 4, 8: 9, 9: 2}, 8)
    2--3--8--9--2
    '''
    # pass
    # REPLACE PASS ABOVE WITH YOUR CODE
    list = []

    if x in D:
        x = D[x]
        while (True):
            if x in D:
                list.append(D[x])
                x = D[x]
            if (list[0] == list[-1] and len(list) > 1):
                break
        print(list)

        str1 = "--".join( str(item) for item in list)
        print(str1)

    else:
        return



if __name__ == '__main__':

    loop({0: 7, 1: 7, 2: 3, 3: 8, 4: 6, 5: 8, 6: 6, 7: 4, 8: 9, 9: 2}, 8)
