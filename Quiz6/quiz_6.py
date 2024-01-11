# Written by *** for COMP9021
#
# Identifies in a grid the rhombuses (of any size)
# that are not included in any other rhombus.
#
# This is a rhombus of size 1:
#        *
#      *   *
#        *
#
# This is a rhombus of size 2:
#        *
#      *   *
#    *       *
#      *   *
#        *
# This is a rhombus of size 3:
#        *
#      *   *
#    *      *
#   *        *
#    *      *
#     *    *
#       *
from collections import defaultdict
from random import seed, randrange
import sys
import math

def is_point_inside_diamond(point, diamond):
    x, y = point
    a, b, c, d = diamond

    # 判断点是否在大菱形的顶点上
    if (x, y) in diamond:
        return True

    # 判断点是否在大菱形的内部
    if (y - a[1]) * (b[0] - a[0]) - (x - a[0]) * (b[1] - a[1]) >= 0 and \
       (y - b[1]) * (c[0] - b[0]) - (x - b[0]) * (c[1] - b[1]) >= 0 and \
       (y - c[1]) * (d[0] - c[0]) - (x - c[0]) * (d[1] - c[1]) >= 0 and \
       (y - d[1]) * (a[0] - d[0]) - (x - d[0]) * (a[1] - d[1]) >= 0:
        return True

    return False
def GetRhombus(grid, dim):
    # print(dim)
    results = defaultdict(list)
    resultsAllPoint = defaultdict(list)
    resultsFilter = defaultdict(list)
    max_size = math.ceil(dim / 2) - 1

    for size in range(1, max_size + 1):
        for i in range(0, dim - size * 2 ):
            for j in range(size, dim - size):
                if(grid[i][j] == "*" and grid[i+size*2][j] == "*" and grid[i+size][j+size] == "*" and grid[i+size][j-size] == "*"):
                    cal = 0
                    for m in range(1,size+1):
                        # print(m)
                        if(grid[i+m][j-m] == "*" and grid[i+m][j+m] == "*" and grid[i+size*2-m][j-m] == '*' and grid[i+size*2-m][j+m] == '*'):
                            # print("success")
                            cal = cal + 1
                            # print(cal,size)
                        if (cal == size):
                            results[size].append((i, j))
    # for item in results:
    #     print(item[1])
    # print(results[1])
    dicPoint = {"top":(),"left":(),"right":(),"bottom":()}
    for i in range(1,size+1):
        # print(i)
        for item in results[i]:
            dicPoint = {"top": (), "left": (), "right": (), "bottom": ()}
            # print(type(item))
            # print(item[0])
            dicPoint["top"] = item
            # item[0] = item[0] + 1
            # item[0] = item[1] - 1
            dicPoint["left"] = (item[0]+i,item[1]-i)
            dicPoint["right"] = (item[0]+i,item[1]+i)
            dicPoint["bottom"] = (item[0]+i*2,item[1])
            # print(dicPoint)
            resultsAllPoint[i].append(dicPoint)
    # for i in range(1,size+1):
    # print(len(resultsAllPoint))
    if (len(resultsAllPoint) == 0):
        return resultsFilter
    if (len(resultsAllPoint) == 1):# 如果全是size为1的就直接输出
        for item in resultsAllPoint[1]:
            # print(item)
            resultsFilter[1].append(item['top'])
        return resultsFilter
    for i in range(1,size):#第一层循环1～n-1的list
        for item in resultsAllPoint[i]:  # 第三层用来循环出i list中的每一个dic
            # print()
            # print("item:", item)
            tmp = 0
            for j in range(i+1,size+1):#第二层循环i~n的list

                for dic in resultsAllPoint[j]:
                    # print("dic:", dic)
                    # print(item["top"][0])
                    polygonlist = []
                    polygonlist.append(dic['left'])
                    polygonlist.append(dic['bottom'])
                    polygonlist.append(dic['right'])
                    polygonlist.append(dic['top'])
                    # print(polygonlist,item['top'])
                    # print(is_point_inside_diamond(item['top'], polygonlist),
                    #       is_point_inside_diamond(item['left'],
                    #    polygonlist),is_point_inside_diamond(item['right'],
                    #    polygonlist),is_point_inside_diamond(item['bottom'], polygonlist)
                    #       )
                    if(
                            is_point_inside_diamond(item['top'], polygonlist) and
                            is_point_inside_diamond(item['left'], polygonlist) and
                            is_point_inside_diamond(item['right'], polygonlist) and
                            is_point_inside_diamond(item['bottom'], polygonlist)
                    ):
                        # print("这个菱形被包含了",item)
                        # print()
                        tmp = tmp + 1

            if (tmp == 0):
                # print("这个菱形被添加了", item)
                resultsFilter[i].append(item['top'])
    # for j in range(2 , size + 1):  # 第二层循环i~n的list
    #     for dic in resultsAllPoint[j]:
    #         print("dic:", dic)
    for item in resultsAllPoint[size]:
        resultsFilter[size].append(item['top'])
    return resultsFilter

def display_grid():
    print('  ', '-' * (2 * dim + 3))
    for row in grid:
        print('   |', *row, '|')
    print('  ', '-' * (2 * dim + 3))

try: 
    for_seed, density, dim = (int(x)
                                  for x in input('Enter three integers, '
                                                 'the second and third ones '
                                                 'being strictly positive: '
                                                ).split()
                             )
    if density <= 0 or dim <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
grid = [['*' if randrange(density) != 0 else ' ' for _ in range(dim)]
            for _ in range(dim)
       ]
# print(grid)
print('Here is the grid that has been generated:')
display_grid()

results = defaultdict(list)

# INSERT YOUR CODE HERE
results = GetRhombus(grid,dim)
print('Here are the rhombuses that are not included in any other:')
for size in sorted(results):
    print(f'Of size {size}:')
    for (i, j) in results[size]:
        print(f'  - with top vertex at location ({i}, {j})')

