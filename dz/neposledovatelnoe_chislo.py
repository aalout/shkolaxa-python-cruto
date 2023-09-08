def find_indexes(numbers):
    diff_indexes = []

    for i in range(1, len(numbers)):
        if numbers[i] - numbers[i-1] > 1:
            diff_indexes.append(i)

    if not diff_indexes:
        return "Не найдено"

    return diff_indexes
n = int(input("Введите количество чисел: "))
numbers = []

for i in range(n):
    num = int(input("Введите число: "))
    numbers.append(num)

result = find_indexes(numbers)
print(result)