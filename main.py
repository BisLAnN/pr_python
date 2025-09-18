# 1
date = input("Введите дату: ")
print("Вы ввели дату: ", date)


# 2
result = (5 - 10) * (2 ** 3) / (15 - 2)
print("Результат выражения: {:.2f}".format(result))


# 3
amount = float(input("Введите сумму, которую Вы положили в банк: "))
bet = float(input("Введите процентную ставку (в виде десятичной дроби): "))
years = float(input("Введите период (в годах): "))

result = amount * (1 + bet) ** years
print(f"Итоговая сумма: {result:.2f} рублей")



# 4
a = float(input("Введите сторону a: "))
b = float(input("Введите сторону b: "))
c = float(input("Введите сторону c: "))

p = (a + b + c) / 2
s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print(f"Площадь треугольника равна: {s:.2f} кв. см.")




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
    print("Корней нет!")




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
print("Результат: ", result)





# 8
a = input("Введите значение первой переменной: ")
b = input("Введите значение первой переменной: ")
a, b = b, a

print("a = ", a)
print("b = ", b)




# 9
n = int(input("Введите число: "))
print("Двоичная: ", bin(n))
print("Восьмеричная: ", oct(n))
print("Шестнадцатеричная: ", hex(n))



# 10
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

print(f"{a} = {a:.3e}")
print(f"{b} = {b:.3e}")
print(f"{c} = {c:.3e}")




# 11
result = (10/2.3 - 3**4) * 0.7 + 9**0.5
result = round(abs(result), 3)
print("Результат с округлением: ", result)



# 12
n = input("Введите четырехзначное число: ")
digits = [int(digit) for digit in n]
print("Цифры введённого числа: ", *digits)




# 13
x = float(input("Введите x: "))
y = float(input("Введите y: "))

result = x * (3.3 + 2*y) - abs(64/(x + y))
print("Результат выражения: {:.2f}".format(result))




# 14
m = float(input("Введите m: "))
n = float(input("Введите n: "))

result = abs(m * (2*m - 1) - 35.5) / (3*n + 0.8*m)**2
print("Результат выражения: {:.2f}".format(result))




if __name__ == "__main__":
    print(f"Результат: {result}")
# khuade_bislan