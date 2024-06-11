numbers = [7, 3, 5, 8, 0, 6, 9, 4]
i = 0
while i < len(numbers):
    if numbers[i] == 0:
        break
    if numbers[i] > 0:
        print(numbers[i])
    i += 1

