import math
import sys
from os.path import exists
import os
import time

def calculate_center(points):
    # 计算图形的中心坐标
    x_sum = sum(x for x, y in points)
    y_sum = sum(y for x, y in points)
    center_x = x_sum / len(points)
    center_y = y_sum / len(points)
    # print(center_x,center_y)
    return center_x, center_y


def rotate_point_around_center(x, y, center_x, center_y, angle_degrees):
    # 将角度转换为弧度
    angle_radians = math.radians(angle_degrees)

    # 将点坐标平移到原点
    translated_x = x - center_x
    translated_y = y - center_y

    # 应用旋转变换公式
    x_prime = translated_x * math.cos(angle_radians) - translated_y * math.sin(angle_radians)
    y_prime = translated_x * math.sin(angle_radians) + translated_y * math.cos(angle_radians)

    # 将坐标平移到中心点
    x_rotated = x_prime + center_x
    y_rotated = y_prime + center_y

    return round(x_rotated, 2), round(y_rotated, 2)


def rotate_shape_around_center(shape_points, angle_degrees):
    # 计算图形的中心坐标
    center_x, center_y = calculate_center(shape_points)

    # 对图形中的每个点应用围绕中心的旋转变换
    rotated_shape = [rotate_point_around_center(x, y, center_x, center_y, angle_degrees) for x, y in shape_points]

    return rotated_shape

def find_convex_vertices(points):
    n = len(points)
    convex_vertices = []

    for i in range(n):
        prev_index = (i - 1) % n
        current_index = i
        next_index = (i + 1) % n

        # 计算前一个、当前和下一个点的向量
        vector1 = (points[current_index][0] - points[prev_index][0], points[current_index][1] - points[prev_index][1])
        vector2 = (points[next_index][0] - points[current_index][0], points[next_index][1] - points[current_index][1])

        # 计算向量的叉积
        cross_product = vector1[0] * vector2[1] - vector1[1] * vector2[0]

        # 如果叉积不为0，说明当前点是一个凸角点
        if cross_product != 0:
            convex_vertices.append(points[current_index])

    return convex_vertices

def point_in_polygon(x, y, polygon):
    n = len(polygon)
    epsilon = 1e-10  # 一个小的偏移值，用于处理浮点数精度问题

    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]

        # 判断点是否在多边形的线段上
        if (abs((x2 - x1) * (y - y1) - (x - x1) * (y2 - y1)) < epsilon) and (
                min(x1, x2) <= x <= max(x1, x2)) and (min(y1, y2) <= y <= max(y1, y2)):
            return False

    # 判断点是否在多边形内
    inside = False
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]

        # 判断点是否在多边形内
        if ((y1 > y) != (y2 > y)) and (x < (x2 - x1) * (y - y1) / (y2 - y1) + x1):
            inside = not inside

    return inside
class PolygonsError(Exception):
    def __init__(self,error):
        self.error = error

class Polygons():
    def __init__(self,filename):
        self.depthList = []
        self.dicStock = []
        self.filename = filename
        self.matrix = []
        # self.path = []
        self.wholePath = []
        # if not exists(filename):
        #     raise PolygonsError("Incorrect input.")

        with open(filename)as file:
            lines = file.readlines()
            for line in lines:
                if(line.isspace()):

                    continue
                else:
                    line = line.replace('\n','')
                    line = line.replace(' ','')
                    char_list = [char for char in line]
                    self.matrix.append(char_list)
                    # self.matrix = [int(binary_str, 2) for binary_str in self.matrix]
        file.close()

        for x in range(len(self.matrix)):
            for y in range(len(self.matrix[0])):
                self.matrix[x][y] = int(self.matrix[x][y])
        if (len(self.matrix) < 2 or len(self.matrix) > 50):
            raise PolygonsError("Incorrect input.")
        if (len(self.matrix[0]) < 2 or len(self.matrix[0]) > 50):
            raise PolygonsError("Incorrect input.")
        for line in self.matrix:
            if(len(line) < 2 or len(line) > 50):
                raise PolygonsError("Incorrect input.")
            for num in line:
                # print(num)
                if(num != 0 and num != 1):
                    raise PolygonsError("Incorrect input.")
            # print(line)
        # self.visited = [[0 for _ in range(len(self.matrix[0]))]for _ in range(len(self.matrix))]
        # for item in self.visited:
        #     print(item)
            # print(content)
        # print(self.filename)
        self.Path = [] #用来存储顶点
        self.Path1 = []
        self.tmp = 2
        for x in range(len(self.matrix)):
            for y in range(len(self.matrix[0])):
                if(self.matrix[x][y] == 1):
                    self.path = []
                    end = (x,y)
                    last = [x,y]
                    self.should_stop = False
                    # self.matrix[x][y] = 0
                    neighborsR = [(x, y + 1), (x + 1, y + 1), (x + 1, y), (x + 1, y - 1), (x, y - 1), (x - 1, y - 1),
                                   (x - 1, y),
                                   (x - 1, y + 1)]
                    for nx, ny in neighborsR:
                        if (0 <= nx < len(self.matrix) and 0 <= ny < len(self.matrix[0]) and self.matrix[nx][
                            ny] == 1):
                            # print(nx,ny)
                            path = []
                            path.append((x,y))
                            # print()
                            # print(self.tmp)
                            #
                            # print("~~~~~~~~~~~~~This is matrix!!!!!")
                            # for line in self.matrix:
                            #     print(line)

                            self.dps(nx, ny, path, end)
                            # print("path路径：", self.path)
                            if (len(self.path) == 1):
                                for point in self.path[0]:
                                    self.matrix[point[0]][point[1]] = self.tmp
                                    # print(point[0], point[1])
                            # self.matrix[x][y] = self.tmp
                    self.tmp = self.tmp + 1


        for line in self.matrix:
            for num in line:
                if(num == 1):
                    raise PolygonsError("Cannot get polygons as expected.")
        # print(self.Path)
        for item in self.Path:
            if (item == []):
                raise PolygonsError("Cannot get polygons as expected.")
        # if (len(self.Path) == 0):
        #     raise PolygonsError("Cannot get polygons as expected.")
        self.area = []
        self.convex = []
        self.perimeter = []
        self.rotations = []
        self.depthOut = []

        areaList = []

        # print(len(self.matrix[0]))
        # print()
        # for line in self.Path:
        #     print(line)
        for m in range(len(self.Path)):
            depth = self.Depth(m)
            area = self.calculate_area(m)
            convex = self.is_convex(m)
            perimeter = self.calculate_perimeter(m)
            areaList.append(float(area))
            Nb_of_invariant_rotations = self.Nb_of_invariant_rotations(m)

            self.perimeter.append(perimeter)
            self.area.append(area)
            self.convex.append(convex)
            self.rotations.append(Nb_of_invariant_rotations)
            self.depthOut.append(depth)

            self.depthList.append(int(depth))
            # print(f"Polygon {m + 1}:")
            # print("    Perimeter:", perimeter)
            # print("    Area:", area)
            # print("    Convex:", convex)
            # print("    Nb of invariant rotations:", Nb_of_invariant_rotations)
            # print("    Depth:", depth)
            # print("    WholeArea", 0.16 * len(self.Path) * len(self.Path[0]))\
            swapped_list = [(t[1], t[0]) for t in self.Path[m]]
            # print(swapped_list)
            # print(self.Path[m])
            dicStock = {"Depth": int, "Poly_Point": [], "Area": float}
            dicStock["Depth"] = depth
            dicStock["Poly_Point"] = swapped_list
            dicStock["Area"] = area
            self.dicStock.append(dicStock)

            # print()
        # print(areaList)
        self.MaxArea = max(areaList)
        self.MinArea = min(areaList)
        self.MaxDepth = max(self.depthList)

        depthSet = set(self.depthList)
        self.depthList = list(depthSet)
        self.depthList.sort()

    def dps(self,x,y,path,end):
        # print(x,y)
        if (self.should_stop):
            return
        if (x == end[0] and y == end[1]):
            # print(path)
            self.path.append(path.copy())
            # print(self.path)
            self.Path1.append(self.path[0].copy())
            self.Path.append(find_convex_vertices(self.path[0]).copy())
            # print("想要获得的matrix~~~~~~~~~~~~~")
            # for item in self.matrix:
            #     print(item)

            # print(self.tmp)
            self.should_stop = True
            self.matrix[x][y] = self.tmp
            # self.matrixC = self.matrix

            return
        self.matrix[x][y] = self.tmp  # 将已访问的点标记为0
        path.append((x,y))

        isx = path[-1][0] - path[-2][0]
        isy = path[-1][1] - path[-2][1]
        # if()
        # print(f"{x}-{y}   {isx},{isy}")
        # last[0] = x
        # last[1] = y

        neighborsR = [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1), (x + 1, y),
                       (x + 1, y - 1), (x, y - 1)]
        neighborsRD = [(x - 1, y), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1), (x + 1, y), (x + 1, y - 1), (x, y - 1),
                      (x - 1, y - 1)]
        neighborsD = [ (x - 1, y + 1), (x, y + 1), (x + 1, y + 1), (x + 1, y), (x + 1, y - 1), (x, y - 1),
                       (x - 1, y - 1), (x - 1, y)]
        neighborsLD = [(x, y + 1), (x + 1, y + 1), (x + 1, y), (x + 1, y - 1), (x, y - 1), (x - 1, y - 1), (x - 1, y),
                      (x - 1, y + 1)]
        neighborsL = [(x + 1, y + 1), (x + 1, y), (x + 1, y - 1), (x, y - 1), (x - 1, y - 1), (x - 1, y),
                       (x - 1, y + 1), (x, y + 1)]
        neighborsLT = [(x + 1, y), (x + 1, y - 1), (x, y - 1), (x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y + 1),
                      (x + 1, y + 1)]
        neighborsT = [(x + 1, y - 1), (x, y - 1), (x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y + 1),
                       (x + 1, y + 1), (x + 1, y)]
        neighborsTR = [(x, y - 1), (x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1), (x + 1, y),
                      (x + 1, y - 1)]

        if(isx == 0 and isy == 1):
            for nx, ny in neighborsR:
                if(0 <= nx < len(self.matrix) and 0 <= ny < len(self.matrix[0]) and self.matrix[nx][ny] == 1):
                    # print(nx,ny)
                    self.dps(nx, ny, path,end)

        elif (isx == 1 and isy == 1):
            for nx, ny in neighborsRD:
                if (0 <= nx < len(self.matrix) and 0 <= ny < len(self.matrix[0]) and self.matrix[nx][ny] == 1):
                    # print(nx,ny)
                    self.dps(nx, ny, path, end)

        elif (isx == 1 and isy == 0):
            for nx, ny in neighborsD:
                if (0 <= nx < len(self.matrix) and 0 <= ny < len(self.matrix[0]) and self.matrix[nx][ny] == 1):
                    # print(nx,ny)
                    self.dps(nx, ny, path, end)

        elif (isx == 1 and isy == -1):
            for nx, ny in neighborsLD:
                if (0 <= nx < len(self.matrix) and 0 <= ny < len(self.matrix[0]) and self.matrix[nx][ny] == 1):
                    # print(nx,ny)
                    self.dps(nx, ny, path, end)

        elif (isx == 0 and isy == -1):
            for nx, ny in neighborsL:
                if (0 <= nx < len(self.matrix) and 0 <= ny < len(self.matrix[0]) and self.matrix[nx][ny] == 1):
                    # print(nx,ny)
                    self.dps(nx, ny, path, end)

        elif (isx == -1 and isy == -1):
            for nx, ny in neighborsLT:
                if (0 <= nx < len(self.matrix) and 0 <= ny < len(self.matrix[0]) and self.matrix[nx][ny] == 1):
                    # print(nx,ny)
                    self.dps(nx, ny, path, end)

        elif (isx == -1 and isy == 0):
            for nx, ny in neighborsT:
                if (0 <= nx < len(self.matrix) and 0 <= ny < len(self.matrix[0]) and self.matrix[nx][ny] == 1):
                    # print(nx,ny)
                    self.dps(nx, ny, path, end)

        elif (isx == -1 and isy == 1):
            for nx, ny in neighborsTR:
                if (0 <= nx < len(self.matrix) and 0 <= ny < len(self.matrix[0]) and self.matrix[nx][ny] == 1):
                    # print(nx,ny)
                    self.dps(nx, ny, path, end)

        path.pop()
        self.matrix[x][y] = 1

    def analyse(self):
        for m in range (len(self.Path)):
            print(f"Polygon {m + 1}:")
            print("    Perimeter:", self.perimeter[m])
            print("    Area:", self.area[m])
            print("    Convex:", self.convex[m])
            print("    Nb of invariant rotations:", self.rotations[m])
            print("    Depth:", self.depthOut[m])
        pass
        # print(self.depthList)
    def calculate_perimeter(self,m):
        # print(self.Path1)
        perimeter1 = 0.0
        tmp = 0
        for i in range(len(self.Path1[m]) - 1):
            # print(self.Path1[m][i])
            x1, y1 = self.Path1[m][i]
            x2, y2 = self.Path1[m][(i + 1)]  # To loop back to the first point
            # print(x1,y1,x2,y2)
            x = abs(x2 - x1)
            y = abs(y2 - y1)
            if(x + y == 1):
                distance = 0.4
                perimeter1 += distance
            if(x + y == 2):
                # distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
                tmp += 1
        #在加上最后两个点之间的长度
        x1,y1 = self.Path1[m][-1]
        x2,y2 = self.Path1[m][0]
        x = abs(x2 - x1)
        y = abs(y2 - y1)
        if (x + y == 1):
            distance = 0.4
            perimeter1 += distance
        if (x + y == 2):
            # distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            tmp += 1
        perimeter1 = "{:.1f}".format(perimeter1)
        perimeter2 = str(tmp) + '*sqrt(.32)'
        if(tmp == 0):
            return perimeter1
        elif(perimeter1 == '0.0'):
            return perimeter2
        else:
            return perimeter1 + ' + ' + perimeter2

    def calculate_area(self,m):
        area = 0
        q = self.Path[m][-1]
        for p in self.Path[m]:
            area += p[0] * q[1] - p[1] * q[0]
            q = p
        area = 0.16 * abs(area) / 2.0
        area = "{:.2f}".format(area)
        return area
    def is_convex(self,m):
        # print(self.Path[m])
        anslist = []
        x1, y1 = self.Path[m][-1]
        x2, y2 = self.Path[m][0]
        x3, y3 = self.Path[m][1]
        # print((x1, y1), (x2, y2), (x3, y3))
        ans = (x3 - x1) * (y2- y1) - (x2 - x1) * (y3 - y1)
        anslist.append(ans)
        # print(ans)

            # flag = True
            # return "no"

        x1, y1 = self.Path[m][-2]
        x2, y2 = self.Path[m][-1]
        x3, y3 = self.Path[m][0]
        # print((x1, y1), (x2, y2), (x3, y3))
        ans = (x3 - x1) * (y2- y1) - (x2 - x1) * (y3 - y1)
        # print(ans)
        anslist.append(ans)
        for i in range(len(self.Path[m]) - 2):
            x1, y1 = self.Path[m][i]
            x2, y2 = self.Path[m][i+1]
            x3, y3 = self.Path[m][i+2]
            # print((x1, y1), (x2, y2), (x3, y3))
            ans = (x3 - x1) * (y2- y1) - (x2 - x1) * (y3 - y1)
            anslist.append(ans)
            # print(ans)

                # flag = True
                # return "no"
        # print(anslist)
        positive = 0
        negative = 0
        for item in anslist:
            if(item > 0):
                positive = positive + 1
            if(item < 0):
                negative = negative + 1
        if(positive > 0 and negative >0):
            return "no"
        else:
            return "yes"
    def Nb_of_invariant_rotations(self,m):
        # print(self.Path[m])
        # original_shape = [(1, 1), (2, 1), (2, 2), (1, 2)]
        Nb_of_invariant_rotation = 0 #一个计数器用来计量
        for rotation_angle in range(1,361):
            tmp = 0
        # 旋转角度
        # rotation_angle = 90  # 旋转45度

        # 应用旋转算法
            rotated_shape = rotate_shape_around_center(self.Path[m], rotation_angle)

            for point in rotated_shape:
                for pathPoint in self.Path[m]:
                    if(point == pathPoint):
                        tmp = tmp + 1
                        break
            if (tmp == len(self.Path[m])):

                        # print(point, pathPoint)
                Nb_of_invariant_rotation = Nb_of_invariant_rotation + 1
        # 输出旋转后的图形坐标
        # print("原始图形坐标:", self.Path[m])
        # print("旋转后的图形坐标:", rotated_shape)
        return Nb_of_invariant_rotation

    def Depth(self,m):
        # print(m)
        # print("Path[m]:",self.Path[m])
        PathCopy = self.Path.copy()
        # print(PathCopy)
        del PathCopy[m]
        # print(PathCopy)

        depth = 0
        for pic in PathCopy:
            for point in self.Path[m]:
            # tmp = 0 #用于计量是否所有的点都在一个图形中
                    if(point_in_polygon(point[0],point[1],pic)):
                        flag  = 1

                        continue
                    else:
                        flag = 0
                        break
            if(flag == 1):
                depth = depth + 1
        return depth
        # for i in range(len()):
        #     point_in_polygon

    def display(self):
        # for dic in self.dicStock:
        #     print(dic)
        # print(self.MaxArea,self.MinArea,self.MaxDepth)
        strHead = r"""\documentclass[10pt]{article}
\usepackage{tikz}
\usepackage[margin=0cm]{geometry}
\pagestyle{empty}

\begin{document}

\vspace*{\fill}
\begin{center}
\begin{tikzpicture}[x=0.4cm, y=-0.4cm, thick, brown]
"""
        # print(len(self.matrix),len(self.matrix[0]))
        # PointList = []
        # PointList.append((0, 0))
        # PointList.append((len(self.matrix[0])-1), 0))
        # PointList.append((len(self.matrix[0])-1), len(self.matrix) - 1))
        # PointList.append((0, len(self.matrix) - 1))
        # for
        strHead = strHead + f'\draw[ultra thick] (0, 0) -- ({len(self.matrix[0])-1}, 0) -- ({len(self.matrix[0])-1}, {len(self.matrix)-1}) -- (0, {len(self.matrix)-1}) -- cycle;\n\n'
        # for dic in self.dicStock:
        #     print(dic)
        if(len(self.dicStock) == 1):
            str = rf"% Depth 0" + '\n'
            for dic in self.dicStock:
                str = str + rf"\filldraw[fill=orange!0!yellow] "
                for tuple in dic["Poly_Point"]:
                    str = str + f"{tuple} -- "
                str = str + f"cycle;" + '\n'
                strHead = strHead + str
        else:
            for depth in self.depthList:
                str = rf"% Depth {depth}" + '\n'
                for dic in self.dicStock:
                    if(dic["Depth"] == depth):
                        tmp = (self.MaxArea - float(dic["Area"]))/(self.MaxArea - self.MinArea)
                        tmp = round(tmp * 100)
                        # print(tmp)
                        # print(dic)
                        # print(self.MaxArea - float(dic["Area"]))
                        # print(self.MaxArea - self.MinArea)
                        # print(round(tmp * 100))
                        str = str + rf"\filldraw[fill=orange!{tmp}!yellow] "
                        for tuple in dic["Poly_Point"]:
                            str = str + f"{tuple} -- "
                        str = str + f"cycle;" + '\n'
                strHead = strHead + str
        strHead = strHead[:-1]
        strHead = strHead + r"""
\end{tikzpicture}
\end{center}
\vspace*{\fill}

\end{document}"""
        strHead = strHead + '\n'
        filename = self.filename.replace('.txt', '.tex')
        # print(filename)


        with open(filename, 'w') as file:
            file.write(strHead)
        # else:
        #     with open(filename,'w')as file:
        #         file.write(strHead)
        # pass

        # print(strHead)
if __name__ == '__main__':
    #incorrect_1.txt
    #incorrect_2.txt
    #wrong_1.txt
    #wrong_2.txt
    #wrong_3.txt
    #polys_3.txt

    polys = Polygons('polys_1.txt')
    polys.analyse()
    polys.display()
    end = time.time()

