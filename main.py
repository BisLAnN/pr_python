# 1
date = input("Введите дату: ")
print("Вы ввели дату: ", date)

# 2
result = (5 - 10) * (2 ** 3) / (15 - 2)
print("Результат выражения: ", result)

# 3
initial, rate, years = 10000, 0.1, 2
amount = initial * (1 + rate) ** years
print(f"Сумма через 2 года: {amount:.2f} рублей")


# 4
a = float(input("Введите сторону a: "))
b = float(input("Введите сторону b: "))
c = float(input("Введите сторону c: "))

p = (a + b + c) / 2
area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print(f"Площадь треугольника: {area:.2f}")


# 5
a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))

D = b**2 - 4*a*c
if D > 0:
    x1 = (-b + D**0.5) / (2*a)
    x2 = (-b - D**0.5) / (2*a)
    print(f"Корни уравнения: {x1}, {x2}")
elif D == 0:
    x = -b / (2*a)
    print(f"Один корень: {x}")
else:
    print("Корней нет")


# 6
seconds = int(input("Введите секунды: "))
days = seconds // (24 * 3600)
seconds %= (24 * 3600)
hours = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60
print(f"{days}:{hours}:{minutes}:{seconds}")


# 7
n = input("Введите число: ")
nn = n * 2
nnn = n * 3
result = int(n) + int(nn) + int(nnn)
print(result)


# 8
a = input("Введите первую переменную: ")
b = input("Введите вторую переменную: ")
a, b = b, a
print("a =", a)
print("b =", b)


# 9
number = 53
print("Двоичная: ", bin(number))
print("Восьмеричная: ", oct(number))
print("Шестнадцатеричная: ", hex(number))


# 10
print(2.754e2)
print(3.2e-3)
print(3.45e0)
# or
numbers = [275.4, 0.0032, 3.45]
for num in numbers:
    print(f"{num} = {num:.3e}")


# 11
result = (10/2.3 - 3**4) * 0.7 + 9**0.5
result = round(abs(result), 3)
print("Результат с округлением: ", result)


# 12
number = input("Введите четырехзначное число: ")
digits = [int(digit) for digit in number]
print("Цифры введённого числа: ", *digits)


# 13
x, y = -4.1, 2
result = x * (3.3 + 2*y) - abs(64/(x + y))
print("Результат выражения: ", result)


# 14
m, n = 2, 5
result = abs(m * (2*m - 1) - 35.5) / (3*n + 0.8*m)**2
print("Результат выражения: ", result)

if __name__ == "__main__":
    print(f"Результат: {result}")
# khuade_bislan