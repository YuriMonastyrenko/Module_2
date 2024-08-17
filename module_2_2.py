first = input("Введите первое число: ")
second = input("Введите второе число: ")
third = input("Введите третье число: ")
if first == second == third:
    print("Вы ввели 3 одинаковых числа.")
elif first == second or first == third or second == third:
    print("Вы ввели 2 одинаковых числа")
else:
    print("Все числа разные.")
