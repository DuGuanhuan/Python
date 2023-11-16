# 初始化一个空列表
numbers = []

while True:
    user_input = input("Enter an integer or q to quit: ")

    # 检查用户是否输入 'q' 来退出程序
    if user_input == 'q':
        break

    try:
        number = int(user_input)  # 尝试将输入的字符串转换为整数
        numbers.append(number)  # 将整数添加到列表中

    except ValueError:
        print("Invalid input. Please enter an integer or 'q' to quit.")

# 显示插入排序前的列表
print(f"Before insertion sort: {numbers}")

# 使用插入排序算法进行排序，降序排列
for i in range(1, len(numbers)):
    key = numbers[i]
    j = i - 1
    while j >= 0 and key > numbers[j]:
        numbers[j + 1] = numbers[j]
        j -= 1
    numbers[j + 1] = key

# 显示插入排序后的列表
print(f"After insertion sort: {numbers}")
