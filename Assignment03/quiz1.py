def selection_sort(arr):
    print(f"Selection Sort Algorithm for {arr}")
    for i in range(0, len(arr) - 1):
        max_index = i
        for j in range(i + 1, len(arr)):
            if arr[max_index] < arr[j]:
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]
        print(f"After round {i}: {arr}")

numbers = []
while True:
    num = input("Enter an integer (or enter quit): ")
    if num.lower() == 'quit':
        break
    numbers.append(int(num))

selection_sort(numbers)
