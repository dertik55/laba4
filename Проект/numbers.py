a = int(input("Введите значение 1: "))
b = int(input("Введите значение 2: "))
c = int(input("Введите значение 3: "))
d = int(input("Введите значение 4: "))

summ1 = a + b
summ2 = c + d

if summ2 != 0:
    razn = summ1 / summ2  
    # Убираем лишние пробелы в формате
    print(f"{razn:.2f}")
else:
    print("Ошибка: деление на ноль.")
