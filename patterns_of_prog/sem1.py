# Императивное:

def sort_list_imperative(numbers):
    n = len(numbers)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if numbers[j] < numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

nums = [64, 25, 12, 22, 11]

print("Отсортированный список (императивно):", sort_list_imperative(nums))

# Декларативное

def sort_list_declarative(numbers):
    array = sorted(numbers, reverse=True)
    return array

print("Отсортированный список (декларативно):", sort_list_declarative(nums))