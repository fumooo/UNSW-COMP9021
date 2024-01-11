# def dfs(matrix, x, y):
#     if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]) or matrix[x][y] == '0':
#         return
#
#     matrix[x][y] = '0'  # 标记为已访问
#     # 处理当前坐标 (x, y)
#     # 这里你可以将 (x, y) 添加到一个列表或其他数据结构中，以表示已访问的正方形边
#
#     # 定义四个方向的偏移量
#     dx = [0, 1, 0, -1]
#     dy = [1, 0, -1, 0]
#
#     for i in range(4):
#         nx, ny = x + dx[i], y + dy[i]
#         dfs(matrix, nx, ny)  # 递归访问邻居
#
# def find_squares(matrix):
#     squares = []
#     for x in range(len(matrix)):
#         for y in range(len(matrix[0])):
#             if matrix[x][y] == '1':
#                 # 开始深度优先搜索
#                 square = []
#                 dfs(matrix, x, y)
#                 squares.append(square)
#     return squares
#
# # 示例用法
# matrix = []  # 填充你的二维列表
# squares = find_squares(matrix)
# print(squares)
import numpy as np


# i = '0'
# print(int(i) + 1)

# def polygon_area(polygon):
#     """
#     compute polygon area
#     polygon: list with shape [n, 2], n is the number of polygon points
#     """
#     area = 0
#     q = polygon[-1]
#     for p in polygon:
#         area += p[0] * q[1] - p[1] * q[0]
#         q = p
#     return abs(area) / 2.0
#
#
# # polygon = np.array([[0, 0], [-1, 1], [0, 2], [1, 1]])
# polygon = [[0, 0], [-1, 1], [0, 2], [1, 1]]
# print(polygon)
# area = polygon_area(polygon)
# print


# import math
#
# def calculate_center(points):
#     # 计算图形的中心坐标
#     x_sum = sum(x for x, y in points)
#     y_sum = sum(y for x, y in points)
#     center_x = x_sum / len(points)
#     center_y = y_sum / len(points)
#     # print(center_x,center_y)
#     return center_x, center_y
#
# def rotate_point_around_center(x, y, center_x, center_y, angle_degrees):
#     # 将角度转换为弧度
#     angle_radians = math.radians(angle_degrees)
#
#     # 将点坐标平移到原点
#     translated_x = x - center_x
#     translated_y = y - center_y
#
#     # 应用旋转变换公式
#     x_prime = translated_x * math.cos(angle_radians) - translated_y * math.sin(angle_radians)
#     y_prime = translated_x * math.sin(angle_radians) + translated_y * math.cos(angle_radians)
#
#     # 将坐标平移到中心点
#     x_rotated = x_prime + center_x
#     y_rotated = y_prime + center_y
#
#     return round(x_rotated,2), round(y_rotated,2)
#
# def rotate_shape_around_center(shape_points, angle_degrees):
#     # 计算图形的中心坐标
#     center_x, center_y = calculate_center(shape_points)
#
#     # 对图形中的每个点应用围绕中心的旋转变换
#     rotated_shape = [rotate_point_around_center(x, y, center_x, center_y, angle_degrees) for x, y in shape_points]
#
#     return rotated_shape
#
# # 示例用法：
# original_shape = [(1, 1), (2, 1), (2, 2), (1, 2)]
#
# # 旋转角度
# rotation_angle = 90  # 旋转45度
#
# # 应用旋转算法
# rotated_shape = rotate_shape_around_center(original_shape, rotation_angle)
#
# # 输出旋转后的图形坐标
# print("原始图形坐标:", original_shape)
# print("旋转后的图形坐标:", rotated_shape)
#
# a = 1
# b = 1.00
# print(a == b)
# def find_convex_vertices(points):
#     n = len(points)
#     convex_vertices = []
#
#     for i in range(n):
#         prev_index = (i - 1) % n
#         current_index = i
#         next_index = (i + 1) % n
#
#         # 计算前一个、当前和下一个点的向量
#         vector1 = (points[current_index][0] - points[prev_index][0], points[current_index][1] - points[prev_index][1])
#         vector2 = (points[next_index][0] - points[current_index][0], points[next_index][1] - points[current_index][1])
#
#         # 计算向量的叉积
#         cross_product = vector1[0] * vector2[1] - vector1[1] * vector2[0]
#
#         # 如果叉积不为0，说明当前点是一个凸角点
#         if cross_product != 0:
#             convex_vertices.append(points[current_index])
#
#     return convex_vertices
#
# # 示例
# polygon = [(21, 21), (21, 22), (21, 23), (21, 24), (21, 25), (21, 26), (21, 27), (21, 28), (22, 28), (23, 28), (24, 28), (25, 28), (26, 28), (27, 28), (28, 28), (28, 27), (28, 26), (28, 25), (28, 24), (28, 23), (28, 22), (28, 21), (27, 21), (26, 21), (25, 21), (24, 21), (23, 21), (22, 21)]
# convex_vertices = find_convex_vertices(polygon)
#
# print("原始图形的所有点坐标:", polygon)
# print("提取的凸角点坐标:", convex_vertices)

# def point_in_polygon(x, y, polygon):
#     n = len(polygon)
#     epsilon = 1e-10  # 一个小的偏移值，用于处理浮点数精度问题
#
#     for i in range(n):
#         x1, y1 = polygon[i]
#         x2, y2 = polygon[(i + 1) % n]
#
#         # 判断点是否在多边形的线段上
#         if (abs((x2 - x1) * (y - y1) - (x - x1) * (y2 - y1)) < epsilon) and (
#                 min(x1, x2) <= x <= max(x1, x2)) and (min(y1, y2) <= y <= max(y1, y2)):
#             return False
#
#     # 判断点是否在多边形内
#     inside = False
#     for i in range(n):
#         x1, y1 = polygon[i]
#         x2, y2 = polygon[(i + 1) % n]
#
#         # 判断点是否在多边形内
#         if ((y1 > y) != (y2 > y)) and (x < (x2 - x1) * (y - y1) / (y2 - y1) + x1):
#             inside = not inside
#
#     return inside
#
# # 示例
# polygon = [(0, 0), (0, 4), (4, 4), (4, 0)]  # 一个正方形
# point = (2, 3)
#
# if point_in_polygon(point[0], point[1], polygon):
#     print(f"点 {point} 在多边形内部")
# else:
#     print(f"点 {point} 不在多边形内部")

tmp = 0
i = 1
while i < 12345:
    if i % 7841 == 0 and i % 23 == 0:
        i += 3

    elif i > 3000:
        i += 2
    else:
        i += 43
    tmp = tmp + 1
print("that's all folks")
print(tmp)