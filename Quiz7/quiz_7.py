# Written by *** for COMP9021
#
# Prompts the user for a ranking of the four horizontal and vertical
# directions, ⬆, ⮕, ⬇ and ⬅, from most preferred to least
# preferred, say d1, d2, d3 and d4.
#
# Determines the path that goes from a given point to another given
# point by following stars in a grid, provided that is possible,
# the path being uniquely defined by the following condition:
# to go from A to B,
# - if it is possible to start taking direction d1,
#   then the path from A to B starts by taking direction d1;
# - otherwise, if it is possible to start taking direction d2,
#   then the path from A to B starts by taking direction d2;
# - otherwise, if it is possible to start taking direction d3,
#   then the path from A to B starts taking direction d3;
# - otherwise, if it is possible to start taking direction d4,
#   then the path from A to B starts by taking direction d4.
#
# The grid and the path, if it exists, are output,
# - the endpoint of the path being represented by a red circle;
# - taking direction North being represented by a yellow square;
# - taking direction East being represented by a brown square;
# - taking direction South being represented by a green square;
# - taking direction West being represented by a purple square;
# - points not on the path being represented by black and white
#   squares depending on whether they are or not occupied by a star.
# (All these characters have been used in quiz 3.)
#
# Also outputs the length of the path, if it exists.


from random import seed, randrange
import sys
import copy

dim = 10

def display_grid():
    print('   ', '-' * (2 * dim + 1))
    for i in range(dim):
        print('   |', ' '.join('*' if grid[i][j] else ' '
                                  for j in range(dim)
                              ), end = ' |\n'
             )
    print('   ', '-' * (2 * dim + 1))
#     print("⬆" + chr(11014))
#     print("⮕" + chr(11157))
#     print(" " + chr(11015))
#     print("⬅" + chr(11013))
#     print("9899" + chr(9899))
#     print("11036" + chr(11036))
#     print("128308" + chr(128308))
#     print("128309" + chr(128309))
#     print("128999" + chr(128999))
#     print("129000" + chr(129000))
#     print("129001" + chr(129001))
#     print("129002" + chr(129002))
#     print("129003" + chr(129003))
def connect(start, end):
    # print(start,end)
    sumPath = []

    path = []
    start_T = (start[0],start[1])
    end_T = (end[0],end[1])


    # print(start_T,end_T)
    if(grid[start[0]][start[1]] != 1 or grid[end[0]][end[1]] != 1):
        print("There is no path joining both points.")
        sys.exit()
    for dir in direction_preferences:
        if(dir == "⬅"):
            directions.append((0, -1))
        elif(dir == "⬆"):
            directions.append((-1, 0))
        elif (dir == "⮕"):
            directions.append((0, 1))
        elif (dir == "⬇"):
            directions.append((1, 0))
    # print(visit)
    # print(directions)
    recursiveFind(start_T, end_T, path)
    # print(Path)
    # print(found_path)
    # print(Path[0])
    print(f"There is a path joining both points, of length {len(Path[0])}:")
    # print(Path[0][1] - Path[0][0])
    for i in range(0,len(Path[0])-1):
        test = (Path[0][i+1][0] - Path[0][i][0], Path[0][i+1][1] - Path[0][i][1])
        if(test == (-1, 0)):
            OutputMax[Path[0][i][0]][Path[0][i][1]] = 129000
        if(test == (0, 1)):
            OutputMax[Path[0][i][0]][Path[0][i][1]] = 129003
        if (test == (1, 0)):
            OutputMax[Path[0][i][0]][Path[0][i][1]] = 129001
        if (test == (0, -1)):
            OutputMax[Path[0][i][0]][Path[0][i][1]] = 129002
        # print(test)
        # print()
    OutputMax[end[0]][end[1]] = 128308
    for i in range (0,dim):
        for m in range (0,dim):
            # print(OutputMax[i][m])
            if(OutputMax[i][m] == 0):
                OutputMax[i][m] = 11036
            if(OutputMax[i][m] == 1):
                OutputMax[i][m] = 11035


    for item in OutputMax:
        print("    ",end='')
        for col in item:

            print(chr(col),end='')
            # print(str(col) + " " ,end='')
        print()
    # REPLACE PASS ABOVE WITH YOUR CODE
def recursiveFind(start,end,path):
    global should_stop
    if(should_stop):
        return
    if(start[0] == end[0] and start[1] == end[1]):#如果起点和终点相连
        path.append(end)
        # print(f"There is a path joining both points, of length {len(path)}")
        # Path.append(path.copy())
        # print(path)
        should_stop = True
        Path.append(path.copy())
        # print()
        return
    visit[start[0]][start[1]] = True
    path.append(start)
    # print(path)

    for dx,dy in directions:
        # print(dx,dy)
        x = start[0] + dx
        y = start[1] + dy
        if is_Point_valid(x,y):
            startT = (start[0] + dx,start[1] + dy)
            # start[0] = start[0] + dx
            # start[1] = start[1] + dy

            recursiveFind(startT,end,path)

    path.pop()
    visit[start[0]][start[1]] = False


def is_Point_valid(dx, dy): #判断即将移动的点合不合法
    return 0 <= dx < dim and 0 <= dy < dim and grid[dx][dy] == 1 and not visit[dx][dy]
# POSSIBLY DEFINE OTHER FUNCTIONS
length = 0
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
try: 
    start = [int(x) for x in input('Enter coordinates '
                                   'of start point:'
                                  ).split()
            ]
    if len(start) != 2 or not (0 <= start[0] < dim)\
                       or not (0 <= start[1] < dim):
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try: 
    end = [int(x) for x in input('Enter coordinates '
                                 'of end point:'
                                ).split()
          ]
    if len(end) != 2 or not (0 <= end[0] < dim)\
                       or not (0 <= end[1] < dim):
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
direction_preferences = input('Input the 4 directions, from most '
                              'preferred to least preferred:'
                             )
if set(direction_preferences) != {'⬆', '⮕', '⬇', '⬅'}:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[int(randrange(density) != 0) for _ in range(dim)]
             for _ in range(dim)
       ]
print('Here is the grid that has been generated:')
display_grid()
print()
visit = [[False for _ in dim] for dim in grid]
OutputMax = grid
# path=[]

directions = []
Path = []
should_stop = False

connect(start, end)

