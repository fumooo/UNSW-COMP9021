my_list = [10, 12, 13, 14, 16, 21, 26, 36, 37, 38, 50]

# 使用列表推导式生成长度为 3 到 11 的所有可能组合
all_combinations = [my_list[i:i + length] for length in range(3, 12) for i in range(len(my_list) - length + 1)]

print(all_combinations)