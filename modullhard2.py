num = int(input("Введите число от 3 до 20: "))
password = ""
for i in range(1, 21):
    for j in range(i+1, 21):
        pair_sum = i + j
        if num % pair_sum ==0:
            password += str(i) + str(j)
print(password)