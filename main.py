# name = "Elena"
# age = 20
# print("Hello,", name)
# print(age)
# print(type(name))
# print(type(age))
# a = 4
# b = 5
# print(a)
# a = b
# print(id(a))  # id
# print(id(b))  #

# a = b = c = 1
# print(a, b, c)

# a, b, c = 5, "Hello", 9.2
# print(a, b, c)

# name_new = "Bob"
# print(name_new)

# PI = 3.14
# print(PI)
# PI = 2
# print(PI)

# a = "Hello"
# print(type(a))
# a = 3
# print(type(a))

# name = "Elena"
# age = 20
# print("Меня зовут: " + name + ". Мне " + str(age) + " лет")
# print("Меня зовут:", name, ". Мне", age, "лет")

# a = 55
# b = 2
# print("a:", a)
# print("b:", b)
# # c = a
# # a = b
# # b = c
# # a, b = b, a
# print("a:", a)  # 2
# print("b:", b)  # 1

# print("строка \
# символов")
# print('строка '
#       'символов')
#
# print("Документ \"script.py\" находится \rпо заданному пути \n\tD:\\\Python\\project")

# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + ", " + s2 + "!\t\t"
# print(s3 * 2)
# print("*" * 40)


# print(464643512321354654684684684)
# print(2.464643512321354654684684684)

# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(6 / 2)  # 3.0
# print(7 / 2)  # 3.5
# print(6 // 2)
# print(7 // 2)
# print(7 % 2)
# print(7 ** 2)

# number = (6 + 4) * (5 ** 2 + 7)
# print(number)   # 113

# num = 10
# num += 5  # num = num + 5
# print(num)  # 15

# num = 4321
# a = num % 10
# # print(a)
# num = num // 10
# # print(num)
# b = num % 10
# # print(b)
# num = num // 10
# # print(num)
# c = num % 10
# # print(c)
# num = num // 10
# # print(num)
# d = num % 10
# # print(d)
# e = a * 1000 + b * 100 + c * 10 + d
# print(e)
#
#
# num1 = 4321
# print(num1)
# res = (num1 % 10) * 1000
# num1 = num1 // 10
# res += (num1 % 10) * 100
# num1 = num1 // 10
# res += (num1 % 10) * 10
# num1 = num1 // 10
# res += (num1 % 10)
# print(res)

# int() - преобразовывает к целочисленному типу данных
# float() - преобразовывает к вещественному типу данных
# str() - преобразовывает к строковому типу данных
# bool() - преобразовывает к булеву типу данных

# num1 = "2"
# num2 = 3
# res = int(num1) + num2
# print(res)
#
# print(int(3.8))
# print(round(3.82))
# print(round(3.8944564654, 5))

# a = 5 / 3
# print(round(a, 2))

# a = '5.2'
# b = 10
# c = float(a) + b
# d = round(c, 1)
# print(type(d))

# a = 1
# b = 2
# print("a:", a, "\nb:", b)
# print("a:", a)
# print("b:", b)

# name = "Викор"
# age = 28
# print("Меня зовут", name, ". Мне", age, "лет.")
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.", age, end=" ", sep="---")
# print("Меня зовут", name, ". Мне", age, "лет.", sep="---", end=" ")
# print("Я учу Python.", end="\n\n")
# print("qqq")
# print(5 + 2, 3 + 4, sep="+")

# print("*** Ваши данные ***")
# name = input("Ваше имя: ")
# city = input("Ваш город: ")
# print(name, city)


# Число 5 в степени 2 равно: 25
# num = int(input("Введите число: "))
# stp = int(input("Введите степень: "))
# sum1 = num ** stp
# print("Число", num, "в степени", stp, "равно:", sum1)

# a = input("Введите число: ")
# b = input("Введите степень: ")
# c = int(a) ** int(b)
# print("Число" + a, "в степени", b, "равно:", c)

# print("Введите четыре числа: ")
# a = int(input("1: "))
# b = int(input("2: "))
# c = int(input("3: "))
# d = int(input("4: "))
# sum1 = a + b
# sum2 = c + d
#
# del1 = sum1 / sum2
# print("Результат:", round(del1, 2))

# a = True
# b = False
# print(a + 5)  # 1 + 5
# print(b * 5)  # 0 * 5

# False = "", 0, False, None
# print(bool("python"))  # True
# print(bool(""))  # False
# print(bool(" "))  # True
# print(bool(0))  # False
# print(bool(-5))  # True
# print(bool(0.5))  # True
# print(bool(0.0))  # False
# print(bool(False))  # False
# print(bool(None))  # False

# test = None
# print(test)
# test = 5
# print(test)

# print(7 == 7)
# print(2 + 5 != 7)
# print(8 > 7)
# print(8 < 7)
# print(8 <= 8)
# print("привет" > "Привет")

# print(2 < 4 < 9)
# print(2 * 5 > 7 >= 4 + 3)
# print(3 * 3 <= 7 >= 2)

# a = 10
# b = 5
# c = a == b
# print(a, b, c)  # 10, 5, False

# print(5 - 3 == 2 and 1 + 3 == 4)  # True (True : True)
# print(5 - 3 == 2 and 1 + 3 < 4)  # False (True : False)
# print(5 - 3 > 2 and 1 + 3 == 4)  # False (False : True)
# print(5 - 3 > 2 and 1 + 3 < 4)  # False (False : False)


# print(5 - 3 == 2 or 1 + 3 == 4)  # True (True : True)
# print(5 - 3 == 2 or 1 + 3 < 4)  # True (True : False)
# print(5 - 3 > 2 or 1 + 3 == 4)  # True (False : True)
# print(5 - 3 > 2 or 1 + 3 < 4)  # False (False : False)

# print(not 9 - 7)
# print(not 7 - 7)

# cnt = 15
# if cnt < 10:
#     cnt += 1
# print(cnt)


# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ запрещен")

# a = 35
# b = 25
# if a > b:
#     print("a > b")
# elif a < b:
#     print("b > a")
# else:
#     print("b == a")

# a = input("Введите первую сторону: ")
# b = input("Введите вторую сторону: ")
# c = input("Введите третью сторону: ")
#
# if a == b == c:
#     print("Равносторонний")
# elif a == b or a == c or b == c:
#     print("Равнобедренный")
# else:
#     print("Разносторонний")

# m = int(input("Введите номер месяца: "))
# # if (m >= 1) and (m <= 12):
# if 1 <= m <= 12:
#     if m == 1 or m == 2 or m == 12:
#         print("Зима")
#     if m == 3 or m == 4 or m == 5:
#         print("Весна")
#     if m == 6 or m == 7 or m == 8:
#         print("Лето")
#     if m == 9 or m == 10 or m == 11:
#         print("Осень")
# else:
#     print("Ошибка ввода данных")
#
#
# num = int(input('Введите номер месяца: '))
# if num > 0 and num < 13:
#     if 1 <= num <= 2 or num == 12:
#         print('Зима')
#     elif 3 <= num <= 5:
#         print('Весна')
#     elif 6 <= num <= 8:
#         print('Лето')
#     else:
#         print('Осень')
# else:
#     print('Введите корректное число')

# day = int(input("Введите день недели (цифрой): "))
# if 1 <= day <= 5:  # day >= 1 and day <= 5
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("пятница")
# elif day == 6 or day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("суббота")
#     if day == 7:
#         print("воскресенье")
# else:
#     print("Такого дня недели не существует!")

# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке ", end="")
#     if n == 1:
#         print(n, "ворона")
#     elif 2 <= n <= 4:
#         print(n, "вороны")
#     else:
#         print(n, "ворон")
#     # if n == 1:
#     #     print(n, "ворона")
#     # if 2 <= n <= 4:
#     #     print(n, "вороны")
#     # if 5 <= n <= 9 or n == 0:
#     #     print(n, "ворон")
# else:
#     print("Ошибка ввода данных")


# a = int(input("Введите число от 1 до 99: "))
# kop = a
# if 11 <= kop <= 14:
#     print(a, "копеек")
# elif 1 <= kop <= 10 or 15 <= kop <= 99:
#     kop = kop % 10
#     if kop == 1:
#         print(a, "копейка")
#     elif 2 <= kop <= 4:
#         print(a, "копейки")
#     else:
#         print(a, "копеек")
# else:
#     print("Некорректный ввод данных")


# Тернарное выражение

# a, b = 30, 20
# minim = a if a < b else b
# print(minim)

# a, b = 50, 30
# print("a == b" if a == b else ("a > b" if a > b else "b > a"))

# if a == b:
#     print("a == b")
# else:
#     if a > b:
#         print("a > b")
#     else:
#         print("b > a")

# a, b = 2, 0
# print("На ноль делить нельзя" if b == 0 else a / b)
#
# num = int(input('Введите делимое: '))
# num2 = int(input('Введите делитель: '))
# print(num / num2 if num2 != 0 else 'На ноль делить нельзя')
#
# print(a / b if b != 0 else "На о  делить нельзя")

# Исключения
# print("Код выше")
# a = 5
# b = 0
# print(a / b)
# print("Код далее")

# try:
#     n = int(input("Введите целое число: "))
#     print(n * 2)
# except ValueError:
#     print("Что-то пошло не так")
#
# print("Код далее")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("Нельзя вводить строки")
# except ZeroDivisionError:
#     print("Нельзя делить на ноль")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Нельзя вводить строки")
#     print("Нельзя делить на ноль")
# else:  # когда в блоке try не возникло исключение
#     print("Все нормально. Вы ввели числа", n, "и", m)
# finally:  # выполняется в любом случае
#     print("Конец программы")

# n = input("Введите первое число: ")  # "9"
# m = input("Введите второе число: ")  # "a"
# try:
#     n = int(n)  # 'a' !!!
#     m = int(m)  # '9'
# except ValueError:
#     n = str(n)
# finally:
#     print(n + m)  # '9' + 'a'


# i = 0
# while i < 5:
#     i += 1  # i = i + 1
#     print("i =", i)


# i = 10
# while i > 0:
#     print("i =", i)
#     i -= 1

# i = 2
# while i <= 20:
#     if i % 2 == 0:
#         print(i)
#     i += 1

# i = 0
# while i < 20:
#     i += 2
#     print("i =", i)

# n = int(input("Укажите количество символов: "))  # 7
# i = 0
# while i < n:
#     print("*", end="")
#     i += 1

# n = int(input("Укажите количество символов: "))  # 7
# while n > 0:
#     print("*")
#     n -= 1

# print("*" * n)

# n = input("Введите целое число: ")
#
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число: ")
#
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")


# i = 0
# while i < 10:  # True
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен!")

# while True:
#     n = int(input("Введите положительное число: "))
#     if n > 0:
#         break
# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i =", i)


# i = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tВложенный цикл: j =", j)
#         j += 1
#     i += 1


# i = 1
# while i <= 9:
#     j = 1
#     while j <= 9:
#         print(i, "*", j, "=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1
# i = 1
# while i <= 5:
#     j = 0
#     while j < 20:
#         if j % 2 != 0:
#             print('+', end='')
#         else:
#             print('-', end='')
#         j += 1
#     print()
#     i += 1


# for element in collection:
#     print(element)

# for i in 'Hello!':
#     print(i)

# i = 1
# for color in 'red', 'orange', 'yellow', 2, 0.3:
#     print(i, "color:", color, type(color))
#     i += 1

# for i in range(n):
#     Тело цикла

# range(start, stop, step)

# for i in range(100, -11, -10):
#     print(i, end=" ")
#
# print()
# j = 100
# while j > 0:
#     print(j, end=" ")
#     j -= 10

# a = int(input("Введите целое число: "))
# for i in range(2, a):
#     # print(i)
#     if a % i == 0:
#         print(i, end=" ")
#     # print(i)


# for i in range(10, 100):  # от 10 по 99
#     if i // 10 == i % 10:
#         print(i, end=" ")
# print()
# for i in range(10, 100):
#     if i % 11 == 0:
#         print(i, end=" ")


# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print('done')

# for i in range(3):
#     print("+++")
#     for j in range(2):
#         print("-----")

# n = int(input('введите длину '))
# m = int(input('введите высоту '))
# for i in range(m):
#     for j in range(n):
#         print('*', end='')
#     print()


# n = int(input("Введите длину прямоугольника"))
# m = int(input("Введите высота прямоугольника"))
# # for i in range(m):
# #     for j in range(n):
# #
# #         print('*', end='')
# #     print()
# for i in range(m):
#     print('*' * n)


# a = int(input("высота прямоугольника "))
# b = int(input("Ширина прямоугольника "))
# for i in range(1, a + 1):
#     for j in range(1, b + 1):
#         if i == 1 or j == 1 or i == a or j == b:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
# i = 0
# while True:  # True
#
#     if i == 6:
#         print(i)
#         break
#     i += 1

# size = int(input("Введите размер поля: "))
# symbol = int(input("Введите количество символов: "))
# for i in range(5):
#     for j in range(3):
#         for n in range(5):
#             for m in range(3):
#                 print("   " if (i + n) % 2 else "*  ", end="")
#         print()


#                 if (i + n) % 2 == 0:
#                     print("*  ", end="")
#                 else:
#                     print("   ", end="")


# for i in range(5):
#     for n in range(5):
#         if (i + n) % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#     print()
# a = 2
# b = 15
# res = 0
# # if a > b:
# #     a, b = b, a
# a, b = (a, b) if a < b else (b, a)
# while a <= b:
#     if a % 2:
#         res += a
#     a += 1
# print(res)
# else:
#     while b <= a:
#         if b % 2:
#             res += b
#         b += 1
#     print(res)

# n = int(input('Введите начало диапазона (включительно): '))  # 2
# m = int(input('Введите конец диапазона (включительно): '))  # 15
# start = n if n < m else m  # 2
# finish = m if n < m else n
# count = 0
# while start <= finish:
#     count += start if start % 2 else 0
#     start += 1
# print('Сумма целых нечетных чисел:', count)

# a = [i * 3 for i in "Hello"]
# print(a)
#
# for i in "Hello":
#     print(i * 3, end=" ")

# num = [i for i in range(30) if i % 2 == 0]
# print(num)

# print([i for i in range(30) if i % 2 == 0])

# Списки (list)

# num = [8, 3, "one", 3.2, [1, 2, 3]]
# # print(num)
# # print(type(num))
# # print(num[1])
# # print(num[-1][1])
# # print(num[-2])
# # num[2] = 256
# # print(num)
# # num[1] += 100
# # num[-1] = 2
# # print(num)
# print("Длина списка:", len(num))

# s = []
# print(type(s))
# b = list()
# print(b)

# s = [5, 1] * 6
# print(s)

# n = list(range(2, 10, 2))
# print(n)
# n2 = [2, 4, 6, 8]
# print(n2)
#
# if n == n2:
#     print("списки равны")
# else:
#     print("списки разные")

# [выражение for переменная in последовательность]
# n = 5
# a = [i ** 2 for i in range(1, n + 1)]
# print(a)

# a = [1, 2, 3]
# b = [5, 6]
# c = b + a
# print(c)
# d = c * 2
# print(d)

# a = [0] * int(input("Введите количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("-> "))
# print(a)

# a = [int(input("-> ")) for i in range(int(input("Кол-во эл-тов: ")))]
# print(a)
# a = [4, 8, 9, 3, 2]
# for i in range(len(a)):  # i - индексы
#     # print(i)
#     print(a[i], end=" ")
# print()
# for elem in a:  # elem - элементы
#     print(elem, end=" ")

# lst = ['один', 'два', 'три']
# for elem in lst:
#     print(elem * 2, end=" ")
# print()
# for i in range(len(lst)):
#     print(lst[i] * 2, end=" ")

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# summa = 0
# for i in a:
#     summa += i if i < 0 else 0
# print('Сумма отрицательных элементов:', summa)

#
# sum1 = 0
# a = [0] * int(input("Введите количество элементов списка: "))
# for i in range(len(a)):
#     a[i] = int(input("-> "))
#     if a[i] < 0:
#         sum1 += a[i]
# print(sum1)

# count = 0
# lst = [int(input('=> ')) for _ in range(int(input('Введите количество элементов ')))]
#
# for i in lst:
#     if i < 0:
#         count += i
# print('сумма отрицательных элементов ', count)

# n = list(range(21, 41))
# print(n)
# k = s = 0
# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         k += 1
#     else:
#         s += n[i]
# print("Количество четных элементов:", k)
# print("Сумма нечетных элементов:", s)
#
#
# n = list(range(21, 41))
# print(n)
# k = s = 0
# for i in n:
#     if i % 2:
#         s += i
#     else:
#         k += 1
# print("количество четных : ", k)
# print("сумма нечетных", s)

# a = [int(input('-> '))for i in range(int(input('Введите количество элементов: ')))]
# count = 0
# summa = 0
# for i in a:
#     summa += i
#     count += 1 if i != 0 else 0
# print('Среднее арифметическое: ', summa/count)

# n = 5
# zero_elem = 0
# sum1 = 0
# lst = [int(input('->')) for _ in range(n)]
# for i in lst:
#     if i != 0:
#         zero_elem += 1
#         sum1 += i
# print('Среднее арифметическое - ', sum1 / zero_elem)

# a = [int(input("->")) for i in range(int(input("Количество элементов: ")))]
# # for i in range(len(a)):
# #     if i % 2 == 0:
# #         print(a[i], end=' ')
#
# for i in range(0, len(a), 2):
#     print(a[i], end=' ')

# a = [0] * int(input("Введите количество элементов списка: "))
# for i in range(len(a)):
#     a[i] = int(input("-> "))
#
# for i in range(len(a)):
#     if i % 2 == 0:
#         print(a[i], end=' ')
#

# a = [7, 8, 2, 1, 17]
# print(a)
# a[0], a[-1] = a[-1], a[0]
# print(a)

# a = [int(input("-> ")) for i in range(int(input("Количество элементов: ")))]
# print(a)


# Срезы

# список[start:stop:step]
# s = [5, 9, 3, 7, 1, 8]
# print(s[1:4])
# print(s[2:])
# print(s[:2])
# print(s[1::2])
# print(s[::-1])
# print(s[-2:2:-1])
# print(s[1:4:-1])
# print(s[10:20])

# s = [1, 2, 3, 4, 5, 6, 7]
# print(s[:])
# # print(s[::-1])
# # print(s[::2])
# # print(s[1::2])
# # print(s[:1])
# # print(s[-1:])
# # print(s[3:4])
# # print(s[4:])
# # print(s[-3:1:-1])
# # print(s[2:5])
# s[1:3] = [0, 0, 0, 0]
# print(s)
# s[1:2] = [20]
# print(s)
# s[3] = 30
# print(s)

# Методы списков
# s = [1, 20, 0, 30, 4, 5, 6, 7]
# print(s)
# t = s.append(99)  # добавляет один элемент в конец списка
# print(s)
# print(t)
# s.extend([9, 8, 7])  # добавляет множество элементов в конец списка
# print(s)
# s.extend('add')
# print(s)
# s.insert(1, 100)  # добавляет заданное значение (второй параметр) по указанному индексу (первый параметр)
# print(s)

# lst = []
# n = int(input("Кол-во элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     # lst.append(x)
#     # lst.extend([x])
#     lst.insert(-1, x)
# print(lst)  # [2,3,1]

# n = int(input('Введите количество элементов списка: '))
# i = 0
# lst = []
# while i < n:
#     x = int(input('Ввведите число кратное 3: '))
#     if x % 3 != 0:
#         print(x, 'число не делится на 3 без остатка')
#     else:
#         lst.append(x)
#     i += 1
# print(lst)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)

# a = [5, 9, 4, 5, 6, 5, 4, 5]
# b = [5, 6, 78, 45, 2, 4]
# c = []
# for i in a:
#     for j in b:
#         if i == j:
#             if i not in c:
#                 c.append(i)
# print(c)

# a = [1, 2, 3, 4, 2]
# b = [11, 22, 33]
# c = []
# print("a =", a)
# print("b =", b)
# if len(b) > len(a):
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):  # range(3, 5)
#         c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(b[i])
#         c.append(a[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
# print(c)

# s = [1, 20, 0, 30, 4, 5, 6, 7, 0, 2]
# # s[2:] = []
# # s[2:6] = []
# s.remove(0)  # удаляет элемент по значению, первое совпадение
# print(s)
# last = s.pop()  # удаляет последний элемент из списка и возвращает удаляемый элемент
# print(last)
# print(s)
# second = s.pop(0)  # удаляет элемент по индексу
# print(second)
# print(s)
# # s.clear()  # очищает список
# # del s[:]
# del s[2]
# print(s)

# s = []
# [s.append(int(input('-> '))) for i in range(int(input('Введите количество элементов: ')))]
# s = [int(input('-> ')) for i in range(int(input('Введите количество элементов: ')))]
# print(s)
# k = int(input('Введите индекс: '))
# # del s[k]
# s.pop(k)
# print(s)

# sp = [int(input('=>')) for i in range(int(input('Введите кол-во значений: ')))]
# x = int(input('Введите число:'))
# for i in range(len(sp)):
#     if x == sp[i]:
#         print('Это число есть в списке')
#         break
# else:
#     print("No")

# print(dir(list))

# s = [1, 20, 0, 30, 4, 0, 5, 6, 7, 0, 2]
# num = s.count(0)  # считает количество заданных значений в списке
# print(num)
#
# ind = s.index(0, 6, -1)  # возвращает положение первого индекса с заданным значением
# print(ind)

# a = [1, 2, 3]
# b = a
# s_copy = a.copy()  # возвращает копию списка, расположенную по другому адресу
# print("a =", a)
# print("b =", b)
# print("s_copy =", s_copy)
# a.append(20)
# b.append(4)
# s_copy.append(444)
# print("a =", a)
# print("b =", b)
# print("s_copy =", s_copy)
# print(id(a))
# print(id(b))
# print(id(s_copy))

# s = ['1', '20', '0', '-30', '04', '0', '5', '6', '7', '0', '2', 'b', 'a', '300']
# s.reverse()  # возвращает None, переставляет элементы списка в обратном порядке
# print(s)
# s.sort(reverse=True)  # reverse=True - сортировка по убыванию
# print(s)
#
# s2 = ["Виталий", "Сергей", "Александр", "Анна"]
# s2.sort(key=len, reverse=True)
# print(s2)
# srt = sorted(s)
# print(sorted(s))
# print(s)
# print(srt)
# print(s)
# print(id(srt))
# print(id(s))

# Генерация случайных данных

# import random
#
# print(random.random())
# print(random.randint(2, 9))  # от 0 по 9 (включительно)
# print(random.randrange(1, 10, 3))

# from random import *
#
# print(randint(2, 9))  # от 0 по 9 (включительно)
# print(randrange(1, 10, 2))
# print(round(uniform(10.5, 25.5), 2))
#
# s = [55, 66, 77, 88, 99, 20, 30, 80, 90]
# print(choice(s))
# print(choices(s, k=3))
# print(s)
# shuffle(s)
# print(s)
#
# mas = [randint(0, 20) for i in range(10)]
# print(mas)

# lst = [5, 3, 2, 4, 1]
# # lst = ['s', 'a', 'r']
# print(len(lst))
# print(sum(lst))  # только с числами
# print(min(lst))
# print(max(lst))

# from random import *

# lst = [randint(0, 100) for i in range(10)]
# max_ = max(lst)
# print(lst)
# print(max_)
# lst.remove(max_)
# lst.insert(0, max_)
# print(lst)

# lst = [randint(0, 100) for i in range(10)]
# print(lst)
# l = lst.pop(lst.index(max(lst)))
# lst.insert(0, l)
# print(lst)

# lst = [randint(-20, 20) for i in range(10)]
# print(lst)
# lst.sort(reverse=True)
# print(lst)


# lst = [randint(0, 100) for i in range(10)]
# print(lst)
# m = min(lst)
# print(m)

# lst = [randint(0, 100) for i in range(10)]
# print(lst)
# m = min(lst)
# print('Min:', m)
# l = lst.index(m)
# print('index min:', l)
# # lst[:l] = []
# del lst[:l]
# print(lst)


# x = list('1a2b3c4d')
# print(x)
# print('a' in x)
# print('e' in x)
# print('a' not in x)
# print('e' not in x)

# lst = []
# # if len(lst) == 0:
# print(bool(lst))
# if not lst:
#     print("Список пустой")

# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
# a = [randint(0, 10) for i in range(n1)]
# b = [randint(0, 10) for j in range(n2)]
# print("Первый список: ", a)
# print("Второй список: ", b)
# c = a + b
# print("Третий список: ", c)
#
# c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
# print("Элементы обоих списков без повторений: ", c)
#
# c = []
# for i in range(len(a)):
#     if a[i] in b and a[i] not in c:
#         c.append(a[i])
# print("Элементы общие для двух списков: ", c)
#
# c = [min(a), min(b), max(a), max(b)]
# print(c)

# n = int(input('Введите размер списка: '))
# lst = []
# for i in range(n):
#     m = randint(0, 100)
#     if m not in lst:
#         lst.append((m))
# print(lst)

# k = int(input("Размер списка: "))  # 6
# s = []
# while len(s) < k:
#     n = randint(1, k)  # с 1 по 6
#     if n not in s:
#         s.append(n)
# print(s)


# n = int(input('Введите число: '))
# s = [i for i in range(1, n+1)]
# shuffle(s)
# print(s)

# m = [
#     [1, 2, 3, 4],  # строка 0
#     [5, 6, 7, 8],  # строка 1
#     [9, 10, 11, 12]  # строка 2
# ]
# print(m)
# print(m[1][2])

# for row in range(len(m)):  # [9, 10, 11, 12, 7, 8]
#     for col in range(len(m[row])):  # 9
#         print(m[row][col], end='\t')
#     print()

# for row in m:
#     for x in row:
#         print(x, end='\t')
#     print()
# print()
# print(m)
# q = [[x**2 for x in row] for row in m]
# print(q)
# for row in q:
#     for x in row:
#         print(x, end='\t\t')
#     print()

# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0

# n, m = int(input('Введите высоту матрицы: ')), int(input('Введите ширину матрицы: '))
#
# matr = [[0 for i in range(m)] for j in range(n)]
# print(matr)
#
# for row in matr:
#     for x in row:
#         print(x, end='\t')
#     print()
# a = [[1, 2, 3], [3, 4, 5], [5, 6, 7], [7, 8, 9]]
# for x, y, z in a:
#     print(x, "+", y, "+", z, "=", x + y + z)

# w, h = 5, 4
# matrix = [[randint(1, 30) for x in range(w)] for y in range(h)]
# for row in matrix:
#     for x in row:
#         print(x, end='\t')
#     print()

# w, h = 3, 4
# matrix = [[randint(-20, 10) for i in range(w)] for j in range(h)]
# count = 0
# for row in matrix:
#     for x in row:
#         if x < 0:
#             count += 1
#         print(x, end='\t\t')
#     print()
# print('Количество отрицательных элементов: ', count)

# w, h = 6, 6
# matrix = [[randint(0, 10) for i in range(w)] for j in range(h)]
# for row in matrix:
#     for x in row:
#         print(x, end='\t')
#     print()
# print()
#
# for row in range(len(matrix)):
#     if row % 2 == 0:
#         for col in range(len(matrix[row])):
#             print(matrix[row+1][col], end='\t')
#         print()
#         for col in range(len(matrix[row])):
#             print(matrix[row][col], end='\t')
#         print()

# w, h = 6, 6  # int(input("Число значений в строке"))
# matrix = [[randint(0, 10) for i in range(w)] for j in range(h)]
# print(matrix)
# for i in range(0, 6, 2):
#     # print(i)
#     matrix[i], matrix[i + 1] = matrix[i + 1], matrix[i]
# print(matrix)

# import math

# print(dir(math))
# num1 = math.sqrt(2)
# print(num1)
# num2 = math.ceil(3.2)
# print(num2)
# num3 = math.floor(3.8)
# print(num3)
# print(math.pi)
#
# radius = 9
# print('Площадь окружности с радиусом', radius, "=>", math.pi * radius ** 2)
# print(round((2 * math.pi * radius), 2))

# import time

# second = time.time()
# print("Секунды с начала эпохи:", second)
# localtime = time.ctime(0)
# print(localtime)
# res = time.localtime(second)
# print(res)
# print(res.tm_year)
# print(time.strftime("Today is %B %d, %Y"))
# print(time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime(799979748)))
#
#
# pause = 5
# print("Program started...")
# time.sleep(pause)
# print(pause, "seconds.")

# text = input("Название напоминания: ")
# local_time = float(input("Через сколько минут: "))
# local_time = local_time * 60
# time.sleep(local_time)
# print(text)

# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# res = finish - start
# print(res)
# 5.000272989273071

# import locale
# locale.setlocale(locale.LC_ALL, 'ru')
#
# print(time.strftime("Сегодня: %B %d, %Y"))


# def hello(word, name):
#     print("Hello,", name, "Say", word)
#
#
# hello("Irina", 'hi')
# hello("Ivan", 'hello')


# def get_sum(a, b):
#     print(a + b)
#
#
# x = 2
# y = 5
# get_sum(x, y)
# n = 7
# m = 9
# get_sum(n, m)
# get_sum('abc', 'def')
# get_sum(2.5, 4.3)


# def symbol(count, a, b):
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end=" ")
#         else:
#             print(b, end=" ")
#
#
# symbol(9, '+', '-')
# print()
# symbol(7, 'X', '0')


# def get_sum(a, b):
#     print(a + b)
#     return a + b
#
#
# x = 2
# y = 5
# res = get_sum(x, y)
# print(res)
# print("!!!", get_sum(1, 8))

# def maximum(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
#
# print(maximum(9, 16))


# def maximum(x, y):
#     if x > y:
#         return x - y
#     else:
#         return x + y
#
#
# a = int(input("a = "))
# b = int(input("b = "))
# print("Результат: ", maximum(a, b))


# def change(lst):
#     # lst[0], lst[-1] = lst[-1], lst[0]
#     start = lst.pop()
#     end = lst.pop(0)
#     lst.append(end)
#     lst.insert(0, start)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))


# def is_greater(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# print(is_greater(10, 5))
# print(is_greater(5, 10))


# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:  #
#         if 'A' <= ch <= 'Z':
#             has_upper = True
#         elif 'a' <= ch <= 'z':
#             has_lower = True
#         elif '0' <= ch <= '9':
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Это надежный пароль")
# else:
#     print("Это ненадежный пароль")

# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# q = 2
# print(get_sum(1, 5, d=q))

# def line(a=20, b='-'):
#     print(b * a)
#
#
# line(10, '*')
# line(10)
# line()

# def get_str(n=20, symbol='-'):
#     return symbol*n
#
#
# print(get_str())
# num = int(input('Введите число: '))
# sym = input('Введите символ: ')
# print(get_str(num, sym))

# def digit_sum(n, even=True):  # 123
#     s = 0
#     while n > 0:
#         cur_digit = n % 10  # 3 2 1
#         if even and cur_digit % 2 == 0:
#             s += cur_digit
#         elif not even and cur_digit % 2:
#             s += cur_digit
#         n //= 10  # 12  1
#     return s
#
#
# print("Сумма четных цифр:")
# print(digit_sum(9874023))
# print(digit_sum(38271))
# print(digit_sum(123456789))
# print("Сумма нечетных цифр:")
# print(digit_sum(9874023, even=False))
# print(digit_sum(38271, even=False))
# print(digit_sum(123456789, even=False))

# def display_info(name, age):
#     print("Name:", name, "\nAge:", age)
#
#
# display_info("Ira", 23)
# display_info(23, "Ira")
# display_info(age=23, name="Ira")
# display_info("Igor", age=23)

# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(id(lt1))
# print(id(lt2))
# print(lt1 == lt2)
# print(lt1 is lt2)
#
# a = 'Hello'
# b = 'Hello'
# print(a == b)
# print(a is b)

# lt1 = [1, 2, 3]
# print(id(lt1))
# lt1.append(4)
# print(lt1)
# lt1.pop(1)
# print(lt1)
# lt1[1] = 'Hello'
# print(lt1)
# print(id(lt1[1]))
# print(id(lt1))

# s = "Hello"
# print(id(s))
# # s += 'World'
# s = s + 'World'
# print(s)
# print(id(s))

# a = 5
# print(id(a))
# a += 1
# print(a)
# print(id(a))

# s = "Hello"
# print(id(s))
# s = s[1:-1]
# print(s)
# print(id(s))

# lt1 = [1, 2, 3]
# print(id(lt1))
# # lt1 = lt1[1:-1]
# # lt1 += [4, 5]
# lt1 = lt1 + [4, 5]
# print(lt1)
# print(id(lt1))

# Кортеж (tuple)
# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# a = 1, 2, 3, 4, 5
# print(type(a))
# print(a)
#
# b = tuple((1, 2, 3, 4, 5))
# print(type(b))
#
# c = tuple("Hello")
# print(c)

# t = (1,)
# print(t)
# print(type(t))

# b = tuple((1, 2, 3, 4, 5))
# print(b)
#
# print(b[3])
# print(b[1:3])
# print(id(b))
# print(id(b[3]))
# b[1] = 3

# s = tuple(int(input("-> ")) for i in range(3))
# print(s)

# s = input("Строка: ")
# a = tuple(s)
# print(a)

# mas = [randint(0, 100) for i in range(10)]
# print(mas)
# tpl = tuple(mas)
# print(tpl)
#
# print(tuple(randint(0, 100) for _ in range(10)))


# print(tuple(2 ** i for i in range(1, 13)))

# t1 = tuple('hello')
# t2 = tuple('world')
# t3 = t1 + t2
# print(t3)
# # print(len(t3))
# # print(t3.count('l'))
# # print(t3.count('a'))
# # print(t3.index('l'))
# # print(t3.index('l', 4))
# # for i in t3:
# #     print(i, end=' ')
# print(t3[2:5])

#
# lst = [
#     [1, 2, 3, 4, 9],
#     [5, 6, 7, 8, 11],
#     [9, 10, 11, 12, 13]
# ]
# row = 0
# for row in lst:
#     for col in row:
#         print(col, end='\t')
#     print()
# print("----------------")
# print(row)
# print("----------------")
# i = 0
# for j in row:  # row = 4
#     # print("*" * 5)
#     # print(col)
#     # print("*" * 5)
#     for row in lst:  # [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
#         # print("=" * 5)
#         # print(lst)
#         # print("=" * 5)
#         print(row[i], end='\t')
#     i += 1
#     print()

# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             # first = tpl.index(el)
#             # second = tpl.index(el, first + 1) + 1
#             # return tpl[first:second]
#             return tpl[tpl.index(el):tpl.index(el, tpl.index(el) + 1) + 1]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# def ran(a, b):
#     return tuple(randint(a, b) for _ in range(10))
#
#
# tpl1 = ran(0, 5)
# tpl2 = ran(-5, 0)
# print(tpl1)
# print(tpl2)
# tpl3 = tpl1 + tpl2
# print(tpl3)
# print('0 =', tpl3.count(0))

# a = 123456
# s = str(a)
# lst = list(s)
# print(lst)
# lst1 = []
# for i in lst:
#     lst1.append(int(i))
# print(''.join(lst))

# t = (10, 11, [1, 2, 3], (4, 5, 6), ['hello', 'world'])
# print(t, id(t))
# print(id(t[4]))
# t[-1][0] = 'new'
# t[4].append('hi')
# print(id(t[4]))
# print(t, id(t))

# def set_elements(lst):
#     return lst
#
#
# print(set_elements([1, 2, 3, 3, 2]))
# print(set_elements([2, 1, 3, 1, 2, 5, 5, 9, 2, 0, 0]))


# def create_tuple(lst):
#     s = []
#     # for i in lst[::-1]:  #
#     #     if i not in s:
#     #         s.append(i)
#     [s.append(i) for i in lst[::-1] if i not in s]
#     return tuple(s)
#
#
# print(create_tuple([1, 2, 3, 3, 2]))
# print(create_tuple([2, 1, 3, 1, 2, 5, 5, 9, 2, 0, 0]))

# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t  # распаковка кортежа
# print(x, y, z)
#
#
# def get_user():
#     name = 'Tom'
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# user = get_user()
# print(user)
# print(user[0])
# name1, age1, is_married1 = user
# print(name1)

# a = (1, 2, 3)
# # del a
# print(a)
# lst = list(a)
# lst.append(4)
# print(lst)
# tpl = tuple(lst)
# print(tpl)

# countries = (
#     ('Германия', 80.2, (
#         ('Берлин', 3.326),
#         ('Гамбург', 1.718))
#      ),
#     ('Франция', 66, (('Париж', 2.2), ('Марсель', 1.6)))
# )
# print(countries, end='\n\n')
# for country in countries:
#     # print(country)
#     countryName, countryPopulation, cities = country
#     print("\nСтрана:", countryName, 'население =', countryPopulation)
#     for city in cities:
#         # print(city)
#         cityName, cityPopulation = city
#         print('\tГород', cityName, 'население =', cityPopulation)

# Множество (set)

# s = {'banana', 'apple', 'orange', 'apple', 'banana'}
# print(type(s))
# print(s)
# print(len(s))
# c = ['hello', 'world']
# a = set(c)
# print(a)

# s = {x * x for x in range(10)}
# print(s)
# print(s)

# num = [1, 2, 2, 2, 3, 3, 4, 4, 5, 6]
# print(num)
# # num = set(num)
# # print(num)
# # num = list(num)\
# num = list(set(num))
# print(num)


# def to_set(element):
#     st = set(element)
#     return st, len(st)
#
#
# print(to_set('я обычная строка'))
# print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))

# t = {'red', 'green', 'blue'}
# # print('green' not in t)
# for i in t:
#     print(i)

# r = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# a = {i for i in r if 'a' not in i}
# a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r}
# a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r if i[1] == 'c'}
# print(a)
#
# for i in r:
#     if i[1] == 'c':
#         print('A' + i[1:] if i[0] == 'a' else 'B' + i[1:])
# if i[0] == 'a':
#     print('A' + i[1:])
# else:
#     print('B' + i[1:])

# a = {'Tom', 'Bob', 'Alice'}
# a.add('Ann')
# print(a)
# # a.remove('Tom')
# # print(a)
# # user = 'Tom'
# # if user in a:
# #     a.remove(user)
# # print(a)
# # a.discard('Bob')
# # print(a)
# a.pop()
# print(a)

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# # c = a.union(b)
# # c = a | b
# # print(c)
# # a.update(b)
# # a |= b
# # c = a & b
# # print(c)
# # a &= b
# # print(a)
# # c = a - b
# c = a ^ b
# print(c)

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
#
# # s = s1.union(s2, s3, s4, s5, s6, s7)
# s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# print(s)
#
# print(len(s))
# print(min(s))
# print(max(s))
# print(sum(s))

# s1 = "Hello"
# s2 = "How are you"
# s = set(s1) & set(s2)
# print(s)


# s1 = set('Python')
# s2 = set('Programming langueg')
#
# s = s1 - s2
# print(s)

# a = set(input("-> "))
# print(a)

# drawing = {'Марина', 'Женя', 'Света'}
# music = {'Костя', 'Женя', 'Илья'}
#
# only = drawing ^ music
# print('Одно хобби: ', only)
#
# both = drawing & music
# print('Два кружка: ', both)
#
# drawing = drawing - both
# print(drawing)
# b = [1, 2, 3, 4, 5]
# s = frozenset(b)
# print(s)
# c = [0, 1, 2]
# s1 = frozenset(c)
# print(s1)
# s -= s1
# print(s)
# a = frozenset({"hello", "world"})
# print(a)

# Словари (dict)

# s = ['one', 'two']
# print(s[1])
# d = {"1": 'one', 2: 'two', 3: "one"}
# print(d)
# print(d[2])

# d = {'one': 1, 'two': 2}
# print(d)
# print(type(d))
#
# d1 = dict(one=1, two=2)
# print(d1)
# print(type(d1))

# a = (
#     ('igor@gmail.com', 'igor'),
#     ('irina@gmail.com', 'irina'),
#     ('anna@gmail.com', 'anna')
# )
# d = dict(a)
# print(d)

# d = {a: a ** 2 for a in range(1, 7)}
# print(d)
# print(d[2])
# d[2] = 15
# print(d)
# d[6] = 4 ** 2
# print(d)

# d = {0: 'text', "one": 45, (1, 2.3): "кортеж", 42: [2, 3, 6, 7], True: 1}
# print(d)
# # print(d[True])
# # print(d[(1, 2.3)])
# # print(d[42][1])
# # print('one' in d)
# # print('two' in d)
# #
# # print(d.keys())
# # if 'one' in d:
# #     print("TRUE")
# # if 'one' in d.keys():
# #     print("TRUE")
# # key = 2
# # # if key in d:
# # #     del d[key]
# # try:
# #     del d[key]
# # except KeyError:
# #     print("Элемента с ключом " + str(key) + " нет в словаре")
# #
# # print(d)
# for key in d:
#     print(key, "->", d[key])

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# pro = 1
# for item in d:
#     pro *= d[item]
# print(pro)

# d = dict()
# d[1] = input("-> ")
# d[2] = input("-> ")
# d[3] = input("-> ")
# d[4] = input("-> ")
# print(d)

# d = {a: input("-> ") for a in range(1, 5)}
# print(d)

# d = {a: input('-> ') for a in range(1, 5)}
# print(d)
# a = int(input('Какой элемент исключить? '))
# if a in d:
#     del d[a]
#     print(d)
# else:
#     print('Такого элемента нет')

# capitals = dict()
# capitals['Россия'] = 'Москва'
# capitals['Италия'] = 'Рим'
# capitals['Испания'] = 'Мадрид'
#
# countries = ['Россия', 'Италия', 'Франция', 'Испания']
#
# for country in countries:
#     if country in capitals:
#         print('Столица страны ' + country + ": " + capitals[country])
#     else:
#         print('В базе нет страны с названием ' + country)

# goods = {
#     '1': ['Core-i3-4330', 9, 4500],
#     '2': ['Core i5-4670K', 3, 8500],
#     '3': ['AMD FX-6300', 6, 3700],
#     '4': ['Pentium G3220', 8, 2100],
#     '5': ['Core i5-3450', 5, 4600],
# }
#
# for i in goods:
#     # print(i)
#     print(i, ') ', goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], 'руб', sep="")

# while True:
#     n = input("№: ")
#     if n != '0':
#         cnt = int(input("Количество: "))
#         goods[n][1] = cnt
#     else:
#         break
#
# for i in goods:
#     print(i, ') ', goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], 'руб', sep="")

# d = {'a': 1, 'b': 2, 'c': 3}
# print(d['b'])
# value = d.get('b')
# print(value)
# print(d)
# # item = d.items()
# # print(item)
# # key = d.keys()
# # print(key)
# # value = d.values()
# # print(value)
# #
# # for i, j in d.items():
# #     print(i, "-> ", j)
# # d.clear()
# # item = d.pop('b', 5)
# # print(item)
# # it = d.popitem()
# # print(it)
# # item = d.setdefault('c', 5)
# # print(item)
# d.update({'a': 7, 'q': 9})  # [('a', 7), ('q', 9)]
# print(d)
# d2 = d.copy()
# print("D =", d)
# print("D2 =", d2)
# d['e'] = 7
# d2['b'] = 5
# print("D =", d)
# print("D2 =", d2)

# a = {'a': 1, 'b': 2}
# b = {'b': 3, 'c': 4}
# # c = a.copy()
# # c.update(b)
# c = b | a
# print(c)

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# d['location'] = d.pop('city')
# print(d)
# new_d = dict()
#
# new_d['name'] = d.pop('name')
# new_d['salary'] = d.pop('salary')
#
# print(d)
# print(new_d)


# d1 = {'name': 'Kelly', 'age':25 , 'salary': 8000, 'city': 'New York'}
# d2 = {}
#
# name = d1.pop('name')
# salary = d1.pop('salary')
# d2['name'] = name
# d2['salary'] = salary
#
# print(d1)
# print(d2)

# a = {
#     'First': {
#         1: 'one',
#         2: 'two',
#         3: 'three'
#     },
#     'Second': {
#         4: 'four',
#         5: 'five'
#     }
# }
# print(a)
#
# for x in a:
#     print(x)
#     for y in a[x]:
#         print('\t', y, ": ", a[x][y], sep="")

# d = {'три': 3, 'один': 11, 'два': 21, 'четыре': 4}
# a = {key: value for key, value in d.items() if value <= 2}
# print(a)

# a = {i: i * 5 for i in [10, 20, 30, 40]}
# print(a)


# a = {i: i * 5 for i in "Hello"}
# print(a)

# value = int(input('-> '))
# # lt = [1, 2, 3, 4, 5]
# a = {i: value for i in range(1, 9)}
# print(a)

# d = dict.fromkeys(['a', 'b'], 100)
# print(d)

# list()
# figures = {1: 'Rectangle', 2: 'Triangle', 3: 'Circle'}
# # value = list(figures.keys())
# # value = list(figures.values())
# value = list(figures.items())
# print(value)

# a = ['one', 1, 2, 3, 'two', 10, 20, 'three', 15, 36, 60, 'four', -20]
# d = dict()
# s = None
#
# for i in a:
#     if type(i) == str:
#         d[i] = []
#         s = i  # 'two'
#     else:
#         d[s].append(i)
# print(d)

# zip()

# d = dict(zip([12, 1, 2], ['Dec', 'Jan', 'Feb']))
# print(d)

# a = [12, 1, 2]
# b = ['Dec', 'Jan', 'Feb']
# f = {k: v for k, v in zip(b, a)}
# print(f)

# a = [1, 2, 3]
# b = [5, 9, 7, 4]
# print(list(zip(a, b)))
#
# print(list(zip(range(5), range(100))))

# a = {'name': 'Igor', 'last_name': 'Doe', 'job': 'Consultant'}
# b = {'name': 'Irina', 'last_name': 'Smith', 'job': 'Manager'}
# c = {'name': 'Irina', 'last_name': 'Smith', 'job': 'Manager'}
#
# for (k1, v1), v2, v3 in zip(a.items(), b.values(), c.values()):
#     print(k1, ' -> ', v1, ", ", v2, ", ", v3, sep="")
#     # print(k2, '-> ', v2)

# a = [(1, 'a', 7), (2, 'b', 8), (3, 'c', 9), (4, 'd', 4)]
# x, y, z = zip(*a)
# print(x)
# print(y)
# print(z)

# lt1 = [2, 21, 3, 32]
# lt2 = ['d', 'a', 'c', 'b']
# # a1 = list(zip(lt2, lt1))
# # print(a1)
# # a1.sort()
# a = sorted(zip(lt1, lt2))
# print(a)

# month = ['January', 'February', 'March']
# total_sales = [52000.00, 51000.00, 48000.00]
# prod_cost = [46800.00, 45900.00, 43200.00]
#
# for sales, cost, m in zip(total_sales, prod_cost, month):
#     res = sales - cost
#     print("Чистая прибыль в", m, "=", res)

# one = {'apple': 0.4, 'orange': 0.35, 'banana': 0.6}
# two = {'pepper': 0.2, 'onion': 0.55, 'banana': 0.4}
# print({**one, **two})  # {'apple': 0.4, 'orange': 0.35, 'banana': 0.4, 'pepper': 0.2, 'onion': 0.55}
#
# for k, v in {**one, **two}.items():
#     print(k, "-> ", v)

# n = int(input("Количество студентов: "))
# stud = {}
# s = 0
# for i in range(n):
#     name = input(str(i + 1) + "-й студент: ")
#     point = int(input("Бал: "))
#     stud[name] = point
#     s += point
#
# avrg = s / n
# print("Средний балл: ", round(avrg, 1))
# print("Студенты с баллом выше среднего: ")
# for i in stud:
#     if stud[i] > avrg:
#         print(i)

# en = ["red", "green", "blue"]
# j = 1
# for i in en:
#     print(j, "-й цвет: ", i, sep="")
#     j += 1

# en = ["red", "green", "blue"]
#
# for j, i in enumerate(en, 1):
#     print(j, "-й цвет: ", i, sep="")

# en = {0: 1, 1: 2, 2: 3}
#
# for i, j in enumerate(en, 1):
#     print(i, ": ", j, "->", en[j], sep="")

# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)


# def func(*args):
#     return args
#
#
# print(func(1))
# print(func(1, 2, 3, 'abc'))
# print(func())

# def summa(*params):
#     res = 0
#     for i in params:
#         res += i
#     return res
#
#
# num1 = summa(1, 2, 3, 4, 5, 6, 7, 8)
# num2 = summa(6, 7, 8)
# print(num1)
# print(num2)


# def to_dict(*args):
#     # dic = {}
#     # for i in args:
#     #     dic[i] = i
#     # return dic
#     return {i: i for i in args}
#
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict('gray', (2, 17), 3.11, -4))


# def func(*num):
#     lst = []
#     a = sum(num) / len(num)
#     print(a)
#     for i in num:
#         if i < a:
#             lst.append(i)
#     return lst
#
#
# print(func(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(func(3, 6, 1, 9, 5))

# def func(a, *args):
#     return a, args
#
#
# print(func(1))
# print(func(1, 2, 3, 'abc'))


# def print_scores(stud, *scores):
#     print("Student name:", stud)
#     for score in scores:
#         print(score, end=" ")
#     print()
#
#
# print_scores("Jonatan", 100, 95, 88, 92, 99)
# print_scores("Rick", 96, 20, 33)


# def func(*args):
#     res = []
#     for i in args:
#         res.append(int(str(i)[::-1]))
#     return res
#
#
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91))

# def reverse_num(n):
#     s = str(n)
#     return int(s[::-1])
#
#
# def func(*args, only_odd=False):
#     res = []
#     for i in args:
#         if not only_odd or (only_odd and i % 2):  # True and i % 2
#             res.append(reverse_num(i))
#     return res
#
#
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91))
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91, only_odd=True))

# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(a='Python'))

# def info(**data):
#     for k, v in data.items():
#         print(k, "->", v)
#     print('*' * 20)
#
#
# info(fist_name="Irina", last_name="Petrova", age=22, phone=1234567890)
# info(fist_name="Igor", last_name="Ivanov", age=36, email='igor@gmail.com', country='Russia', phone=6789012345)

# def db(**kwargs):
#     my_dict.update(kwargs)
#
#
# my_dict = {'one': 'first'}
# db(k1=22, k2=31, k3=11, k4=91)
# db(name='Bob', age=31, weight=61, eyas_color='gray')
# print("my_dict =", my_dict)


# def func1(*args):
#     print(args[0])
#
#
# def func2(**kwargs):
#     print(kwargs['one'])
#
#
# func1(1, 2, 3, 4, 5)
# func2(one=123, two=456)


# def func(a, *args, one=True, **kwargs):
#     return args, kwargs, a, one
#
#
# print(func(5, 9, 7, 8, 6, b=2, one=False, c=3, d=4))


# Область видимости (scope)

# name = "Tom"
#
#
# def hi():
#     print("Hello", name)
#
#
# def bye():
#     global name
#     name = "Bob"
#     print("Good bye", name)
#
#
# def func():
#     global surname
#     name = "Nike"
#     surname = "Ivanov"
#     print("name:", name)
#
#
# hi()
# bye()
# func()
# print(name)
# print(surname)


# i = 5
#
#
# def func(arg=i):
#     print(arg)
#
#
# i = 6
# func()  # 5
# print(i)


# def add_two(a):
#     x = 2
#     return a + x
#
#
# print(add_two(3))
# print(x)

# x = 3
#
#
# def func(a):
#     x = 2
#
#     def inner():
#
#         print("x =", x)
#         return a + x
#
#     return inner()
#
#
# print(func(5))  # 7


# import builtins
#
# print(dir(builtins))
#
#
# def square(figure_type, **kwargs):
#     print(kwargs['d2'])
#
#
# print(square(figure_type='rhombus', d1=10, d2=8))

# Вложенные функции

# def outer_func(who):
#     def inner_func():
#         print("Hello,", who)
#
#     inner_func()
#
#
# outer_func("world!")
#
# def func1():
#     a = 6  # 2
#
#     def func2(b):
#         # a = 4  # 5
#         print(a)
#         print("Сумма:", a + b)  # 6
#
#     print("a:", a)  # 3
#     func2(4)  # 4
#
#
# func1()  # 1


# x = 25
# t = 0
#
#
# def fn():
#     global t
#     a = 30
#
#     print("global:", x)  # 25
#
#     def inner():
#         nonlocal a
#         a = 35
#         print("nonlocal:", a)  # 35
#
#     inner()
#     print(a)
#     t = a
#
#
# fn()
# z = x + t  # 25 + 35 = 60
# print('results:', z)

# x = 5
#
#
# def fn1():
#     x = 25
#
#     def fn2():
#         # x = 33
#
#         def fn3():
#             nonlocal x
#             x = 55
#
#         fn3()
#         print('fn2.x =', x)
#
#     fn2()
#     print('fn1.x =', x)
#
#
# fn1()
# print('x =', x)


# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         # print(a, b)
#
#         a = a1 + a2
#         b = b1 + b2
#         print(a, b)
#
#     inner()
#     return [a, b]
#
#
# res = outer(2, 3, -1, 4)
# print(res)


# def increment(number):
#     def inner():
#         return number + 1
#     return inner()
#
#
# res = increment(10)
# print(res)

# Замыкания

# def outer(n):
#     def inner(x):
#         return n + x
#     return inner
#
#
# # print(outer(5)(10))
#
# res = outer(5)
# print(type(res))
# q = res(10)
# print(q)
# print(res(2))
#
# res2 = outer(7)
# print(res2(5))
#
# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         # a = 20
#         a = a + 1
#         # b = b + "_new"
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())


# def func(city):
#     s = 0
#
#     def inner():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return inner
#
#
# res1 = func('Москва')
# res1()
# res1()
#
# res2 = func("Сочи")
# res2()
# res2()
# res2()
#
# res1()


# students = {
#     'Alice': 100,
#     'Bob': 67,
#     'Chris': 85,
#     'David': 75,
#     'Elise': 54,
#     'Fiona': 35,
#     'Grace': 69
# }
#
#
# def make_classifier(lower, upper):
#     def classify_student(exam):
#         return {k: v for k, v in exam.items() if lower <= v < upper}
#
#     return classify_student
#
#
# A = make_classifier(80, 101)
# B = make_classifier(70, 80)
# C = make_classifier(50, 70)
# D = make_classifier(0, 50)
# print(A(students))
# print(B(students))
# print(C(students))
# print(D(students))


# def func(a, b):
#     def add():
#         return a + b
#
#     def sub():
#         return a - b
#
#     def mul():
#         return a * b
#
#     def replace():
#         print("qqqq")  # pass
#
#     replace.add = add
#     replace.sub = sub
#     replace.mul = mul
#     return replace
#
#
# obj1 = func(5, 2)
# print(obj1.add())
# print(obj1.sub())
# print(obj1.mul())
#
# obj2 = func(15, 12)
# print(obj2.add())
# print(obj2.sub())
# print(obj2.mul())
# obj2()


# Анонимные функции, lambda-выражения

# (lambda x, y: print("res =", x == y))(1, 2)
# print("res =", (lambda x, y: x + y)('a', 'b'))
#
# func = (lambda x, y: x + y)
# print(func(1, 2))
# print(func('a', 'b'))

# print((lambda x, y: x ** 2 + y ** 2)(2, 5))

# summ = lambda a=1, b=2, c=3: a + b + c
#
# print(summ())
# print(summ(10))
# print(summ(10, 20))

# func1 = lambda *args: args
#
# print(func1(1, 2, 3, 4))
# print(func1('a', 'b'))

# c = (lambda x: x * 2,
#      lambda x: x * 3,
#      lambda x: x * 4)
#
# for t in c:
#     print(t("abc_"))


# def inc1(n):
#     def wrap(x):
#         return x + n
#
#     return wrap
#
#
# f1 = inc1(42)
# print(f1(3))
#
#
# def inc(n):
#     return lambda x: x + n
#
#
# f = inc(42)
# print(f(3))
#
# inc2 = (lambda n: (lambda x: x + n))
# # f2 = inc2(42)
# # print(f2(3))
# print(inc2(42)(3))
#
# print((lambda n: (lambda x: x + n))(42)(3))


# print((lambda a: (lambda b: (lambda c: a + b + c)))(2)(4)(6))

# def func(i):
#     return i[1]
#
#
# d = {'b': 15, 'a': 10, 'c': 24}
# lst = list(d.items())
# print(lst)
# # lst.sort(key=lambda i: i[1], reverse=True)
# lst.sort(key=func, reverse=True)
# print(lst)
# dict1 = dict(lst)
# print(dict1)

# players = [{'name': 'Антон', 'last name': 'Бирюков', 'raiting': 9},
#            {'name': 'Алексей', 'last name': 'Бодня', 'raiting': 10},
#            {'name': 'Федор', 'last name': 'Сидоров', 'raiting': 4},
#            {'name': 'Михаил', 'last name': 'Семенов', 'raiting': 6}]
#
# # players1 = ['Наталья', 'Виктор', 'Саша']
# #
# # players1.sort(key=len)
# # print(players1)
# res = sorted(players, key=lambda item: item['last name'])
# print(res)
# # players.sort(key=lambda item: item['last name'])
# # print(players)
# res = sorted(players, key=lambda item: item['raiting'])
# print(res)
# res = sorted(players, key=lambda item: item['raiting'], reverse=True)
# print(res)


# a = [(lambda x, y: x + y), (lambda x, y: x - y), (lambda x, y: x * y), (lambda x, y: x / y)]
# b = a[2](12, 5)
# print(b)

# a = {'one': lambda x: x-1, 'two': lambda x: abs(x) - 1, 'three': lambda x: x}
# b = [-3, 10, 0, 2]
# for i in b:
#     if i < 0:
#         print(a['two'](i))
#     elif i > 0:
#         print(a['one'](i))
#     else:
#         print(a['three'](i))

# d = {
#     1: (lambda: print('Понедельник')),
#     2: (lambda: print('Вторник')),
#     3: (lambda: print('Среда')),
#     4: (lambda: print('Четверг')),
#     5: (lambda: print('Пятница')),
#     6: (lambda: print('Суббота')),
#     7: (lambda: print('Воскресенье')),
# }
#
# d[5]()

# maximum = (lambda a, b: a if a > b else b)
# print(maximum(15, 23))


# minimun = (lambda a, b, c: a if a < b else (b if b < c else c))
# print(minimun(1, 18, 2))

# maximum = (lambda a, b, c: a if (a < b and a < c) else (b if b < a and b < c else c))
# print(maximum(11, 12, 5))


# Функция map()

# def multiple(t):
#     return t * 2


# lst = [2, 8, 12, -5, -10]
#
# # print(list(map(multiple, lst)))
# print(list(map(lambda i: i > 2, lst)))


# t = (2.88, -1.75, 100.55)
#
# print(list(map(lambda x: str(x), t)))
#
#
# a = ['2.88', '-1.75', '100.55']
# # b = list(map(float, a))
# # print(b)
# print(list(map(int, map(float, a))))

# areas = [3.578945, 5.789456, 7.456789, 56.4123456, 9.0123456, 32.7789456]
# print(list(map(round, areas, (2, 6, 4, 3))))

# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
#
# lst = dict(map(lambda x, y: (x, y), st, num))
# print(lst)
# tp = dict(lst)
# print(tp)

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
#
# print(list(map(lambda x, y: x + y, l1, l2)))


# filter(func, iterable)

# t = ('abcd', 'abc', 'cdefg', 'def', 'ghi')
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)
#
# b = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# res = list(filter(lambda s: 75 < s < 88, b))
# print(res)


# from random import *
#
# lst = [randint(1, 40) for i in range(10)]
# print(lst)
# res = list(filter(lambda s: 10 <= s <= 20, lst))
# print(res)

# lst = [45, 55, 60, 37, 100, 105, 220]
# res = list(filter(lambda s: s % 15 == 0, lst))
# print(res)

# Декораторы

# def hello():
#     return "Hello, I am func 'hello'"
#
#
# def super_func(func):
#     print("Hello, I am func 'super_func'")
#     print(func())
#
#
# super_func(hello)
#
# test = hello
# print(test())

# def my_decorator(func):
#     def wrap():
#         print('Code before')
#         func()
#         print('Code after')
#     return wrap
#
#
# def func_test():
#     print("Hello, I am func 'func_test'")
#
#
# test = my_decorator(func_test)
# test()
# test()
# test()


# def my_decorator(func):  # декорирующая функция
#     def wrap():
#         print('Code before')
#         func()
#         print('Code after')
#     return wrap
#
#
# @my_decorator  # декоратор
# def func_test():  # декорируемая функция
#     print("Hello, I am func 'func_test'")
#
#
# @my_decorator
# def hello():
#     print("Hello, I am func 'hello'")
#
#
# func_test()
# print()
# hello()

# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#
#     return wrap
#
#
# @bold
# @italic
# def hello():
#     return "text"
#
#
# print(hello())

# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print("Вызов функции: ", count)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print("Hello")
#
#
# @cnt
# def bye():
#     print("Good bye")
#
#
# hello()
# hello()
# bye()
# hello()
#
# bye()
#
# bye()
# bye()
# def args_decorator(fn):
#     def wrap(arg1, arg2):
#         print("*" * 50)
#         fn(arg1, arg2)
#         print("*" * 50)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#
#
# print_full_name("Ирина", "Лаврова")


# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         fn(*args, **kwargs)
#         print("*" * 50)
#         print("args:", args)
#         print("kwargs:", kwargs)
#         print("*" * 50)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(a, b, c, study='Python'):
#     print(a, b, c, "изучают", study)
#
#
# @args_decorator
# def hello():
#     print("Hello")
#
#
# print_full_name("Ирина", "Борис", "Светлана", study="JavaScript")
# print()
# print_full_name("Владимир", "Екатерина", "Виктор")
# print()
# hello()
# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end=" ")
#             fn(x, y)
#         return wrap
#     return args_dec
#
#
# @decor("Сумма:", "+")
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность:", "-")
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)


# def multiply(n):
#     def return_mult(fn):
#         def wrap(num):
#             print('Результат:', end=" ")
#             return fn(num) * n
#
#         return wrap
#
#     return return_mult
#
#
# @multiply(3)
# def return_num(num):
#     return num * 2
#
#
# print(return_num(5))

# def typed(*args, **kwargs):
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:
#                     # raise TypeError("Некорректный тип данных")
#                     # print("Некорректный тип данных")
#                     return "Некорректный тип данных"
#             for k in kwargs:
#                 if type(f_kwargs[k]) != kwargs[k]:
#                     # raise TypeError("Некорректный тип данных")
#                     return "Некорректный тип данных"
#             return fn(*f_args, **f_kwargs)
#         return wrap
#     return wrapper
#
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return x + y + z
#
#
# @typed(str, str, z=int)
# def typed_fn3(x, y, z="Hello! "):
#     return (x + y) * z
#
#
# print(typed_fn(3, 4, 5))
# print(typed_fn(3, 4, "Doge"))
# print(typed_fn2("Hello, ", "World", "!"))
# print(typed_fn3("Hello_", "World___", z=5))
# print(typed_fn3("Hello, ", "World", z="!!!"))


# def avr(fn):
#     def wrap(*args):
#         print(*args)
#         print(args)
#         a = ''
#         for i in args:
#             a += str(i) + ", "
#         print('Среднее арифметическое чисел', a[:-2], '=', fn(*args) / len(args))
#
#     return wrap
#
#
# @avr
# def summer(*ar):
#     print('Сумма чисел', *ar, '=', sum(ar))
#     return sum(ar)
#
#
# summer(2, 3, 3, 4)
# def decor(tx=None, decor_text=''):
#     def wrapper(fn):
#         def wrap(*args):
#             print(decor_text, end="")
#             fn(*args)
#
#         return wrap
#
#     if tx is None:
#         return wrapper
#     else:
#         return wrapper(tx)
#
#
# @decor
# def hello_world2(text):
#     print(text)
#
#
# @decor(decor_text="Hello, ")
# def hello_world(text):
#     print(text)
#
#
# hello_world2("Hi!")
# hello_world("world!")


# print(int('100', 2))
# print(int('100', 8))
# print(int('100', 16))
# print(int('100', 10))
# print(int('100'))

# print(bin(18))  # 0b10010  # 0B
# print(oct(18))  # 0o22     # 0O
# print(hex(18))  # 0x12     # 0X
#
# print(0b100 + 0o20)  # 4
# print(0o20)  # 16
# print(0x11 + 3)

# q = 'Pyt'
# w = 'hon'
# e = q + w
# print(e)
# # print(e * 3)
# # print('e' in e)
# # print(e[-1:0:-1])
# e = e[:3] + 't' + e[4:]
# print(e)


# def change_char(s, c_old, c_new):
#     s2 = ""
#     for i in s:
#         if i != c_old:
#             s2 += i
#         else:
#             s2 += c_new
#     return s2
#
#
# st = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# st2 = change_char(st, 'N', 'P')
# print("st1 =", st)
# print("st2 =", st2)

# print(u"Привет")
# print(r'C:\file.txt')  # "сырые" строки
# print('C:\\file.txt')
# print(r'C:\file.txt\\'[:-1])
# print(r'C:\file.txt' + "\\")
# print('C:\\file.txt\\')

# name = "Дмитрий"
# age = 25
# print("Меня зовут " + name + ". Мне " + str(age) + " лет")
# print("Меня зовут ", name, ". Мне ", age, " лет", sep="")
# print(f"Меня зовут {name}. Мне {age} лет")
#
# print(f"{round(2.356789, 2)}")
# print(f"{2.356789:.2f}")

# x = 10
# y = 5
# print(f"{x} x {y} / 2 = {int(x * y / 2)}"
#       f" - выражение")

# d = 74
# print(f"{{{{{d}}}}}")


# def binary(ch):
#     s = ''
#     while ch > 0:
#         s = str(ch % 2) + s
#         ch //= 2
#     return s
#
#
# while True:
#     n = int(input("-> "))
#     if n != 0:
#         print(binary(n))
#     else:
#         break

# dir_name = 'doc'
# file_name = 'data.txt'
# print(fr'home\{dir_name}\{file_name}')
# print("home\\" + dir_name + "\\" + file_name)

# s = """<div>
#     <a href="#">content</a>
# </div>
# """
# print(s)
# s1 = '''<div>
#     <a href="#">content</a>
# </div>
# '''
# print(s1)

# def square(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     a = 5
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)


# import math
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * math.pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)

# print(ord('a'))
# print(ord('р'))
#
# while True:
#     n = input("-> ")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break

# my_str = "Test string for me"
# arr = [ord(x) for x in my_str]
# print(arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print(arr)
# arr += [x for x in [ord(x) for x in input("-> ")[:3]] if x not in arr]  # [:6:2] - пробелы
# print(arr)
# if arr[-1] in arr[:-1]:
#     print(arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)

# print(chr(97))
# print(chr(35))
# print(chr(8364))

# a = 97
# b = 122
# if a > b:
#     for i in range(b, a + 1):
#         print(chr(i), end=' ')
# else:
#     for i in range(a, b + 1):
#         print(chr(i), end=' ')

# a, b = 97, 122
# if b < a:
#     a, b = b, a
# while a <= b:
#     print(chr(a) + " ", end="")
#     a += 1


# print('apple' == 'appLe')
# print('apple' > 'Apple')  # 97 > 65
# print(ord('a'))  # 97
# print(ord('A'))  # 65


# from random import randint
#
# SHORTEST = 6
# LONGEST = 16
# MIN_ASCII = 33
# MAX_ASCII = 126
#
#
# def random_password():
#     random_length = randint(SHORTEST, LONGEST)
#     res = ""
#     for i in range(random_length):
#         random_char = chr(randint(MIN_ASCII, MAX_ASCII))
#         res += random_char
#     return res
#
#
# print("Ваш случайный пароль:", random_password())

# print(dir(str))

# s = "hello, WORLD! I am learning Python."
# print(s.capitalize())  # Hello, world! i am learning python.
# print(s.lower())  # hello, world! i am learning python.
# print(s.upper())  # HELLO, WORLD! I AM LEARNING PYTHON.
# print(s.swapcase())  # HELLO, world! i AM LEARNING pYTHON.
# print(s.title())  # Hello, World! I Am Learning Python.
#
# print(s.count("l", 3))  # подсчитывает количество вхождений подстроки в строку
# print(s.find("Python1"))  # ищет в строке заданную подстроку, если она найдена, то возвращает индекс первого
# # вхождения подстроки, если нет - то возвращает "-1"

# a = "один два"
# b = a[:a.find(" ")]
# c = a[a.find(" ") + 1:]
# print(c + " " + b)

# a = 'ab12c59p7dq'
# digits = []
#
# # for i in a:
# #     if i in '1234567890':
# #         digits.append(int(i))
# # print(digits)
# b = '1234567890'
# for i in a:
#     if b.find(i) != -1:
#         digits.append(int(i))
# print(digits)

# s1 = 'ab12c59ptdq'
# s2 = []
# for i in s1:
#     try:
#         s2.append(int(i))
#     except ValueError:
#         continue
# print(s2)

# print(s)
# print(s.index("Python"))  # ищет в строке заданную подстроку, если она найдена, то возвращает индекс первого
# # вхождения подстроки, если нет - то возвращает исключение ValueError

# print(s.rfind('h'))
# print(s.rindex('h'))

# a = 'I am learning Python. hello, WORLD!'
# # first = a.find('h')
# # last = a.rindex('h')+1
# # print(a[:first] + a[last:])
# print(a[:a.find('h')] + a[a.rindex('h')+1:])


# print('abc123'.isalnum())  # определяет состоит ли строка из цифр или букв
# print('ABCabc'.isalpha())  # определяет состоит ли строка из букв
# print('123'.isdigit())  # определяет состоит ли строка из цифр
# print('abc2'.islower())  # определяет состоит ли строка из строчных букв
# print('ACD3'.isupper())  # определяет состоит ли строка из заглавных букв


# print('py'.center(10, "-"))  # выравнивание строки по центру
# print(' py '.center(30, "*"))

# print("    py".lstrip())  # удаляет пробельные символы слева
# print("py    ".rstrip())  # удаляет пробельные символы справа
# print("   py ".strip())  # удаляет пробельные символы и слева и справа
#
# print("https://www.python.org".lstrip('p/:ths'))
# print("py.$$$;".rstrip(';$.'))
#
# print("https://www.python.org".lstrip('htps:/w').rstrip("org."))
# print("https://www.python.org".strip('htps:/worg.'))
#
# print("http://www.python.org".strip('/:pthsworg').strip('.'))

# s = "11 23 44 55 23 22 23 77 99"
# s_old = input("Заменяемая подстрока: ")  # 23
# s_new = input("Новая подстрока: ")  # !!!
# i = s.find(s_old)  # 3
# # print(i)
# while i != -1:
#     ll = len(s_old)  # 2
#     s = s[0:i] + s_new + s[i+ll:]  # 11 !!! 44 55 23 22    # 11 !!! 44 55 !!! 22
#     i = s.find(s_old)  # 13
# print(s)  # 11 !!! 44 55 !!! 22

# st = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# print(st)
# print(st.replace("Nython", "Python", 2))  # заменяет вхождение подстроки в строке

# s = "-"
# seq = ("a", "b", "c")
# print(s.join(seq))  # a-b-c
#
# print("..".join(['1', '2']))  # объединяет итерируемую последовательность (список, кортеж, другая строка) в одну
# # строку через заданный символ разделитель
#
# print(":".join("Hello"))

# print("Строка разделенная пробелами".split())  # делит строку на список из подстрок
# # print("Строка_разделенная_пробелами".split("_"))
# # print("Строка разделенная пробелами".split("а"))
#
# print('www.python.org.ru.'.split("."))

# a = list(map(int, input("-> ").split()))
# print(a)
# print(type(a[0]))


# a = input('Введите ФИО: ').split()
# print(a)
# print(a[0], ' ', a[1][0], '.', a[2][0], '.', sep='')


# s = input('ФИО: ').split()
# print(f'{s[0]} {s[1][0]}. {s[2][0]}.')


# print('www.python.org.ru.'.split(".", 2))
# print('www.python.org.ru.'.rsplit(".", 2))
#
# print('www...python...org'.split("..."))

# s = 'В строке пробел заменить на звездочку'.split()
# print('*'.join(s))

# Регулярные выражения

# import re

# from re import *

# s = "Я ищу совпадения в 2023 году. И я их найду в 2000000000 счёта. 9578 19_4 5"
# # reg = r'^\w+\s\w+'
# reg = r'\w+\s\w+$'
# # reg = r'[А-яё.]'  # [А-Яа-яЁё]
# # reg = r'[0-59]'
# # reg = r'[12][90][0-9][0-9]'
#
# # print(s.find(reg))
# # print(re.findall(reg, s))  # ['я', 'я']  возвращает список, содержащий все совпадения
# # print(re.findall('12', s))  # []
#
# print(re.search(reg, s))  # месторасположение первого совпадения объекта
# # print(re.search(reg, s).span())
# # print(re.search(reg, s).start())
# # print(re.search(reg, s).end())
# # print(re.search(reg, s).group())
#
# # print(re.match(reg, s))  # поиск по заданному шаблону в начале строки
#
# print(re.split(reg, s, 1))  # возвращает список, в котором строка разбита по шаблону
#
# print(re.sub(reg, "!", s, 1))  # поиск и замена
#
# # print(re.findall(reg, s))
#
# # Повторения
# # + - от 1 до бесконечности
# # * - от 0 до бесконечности
# # ? - 0 или 1
#
# # s1 = "Ели{-ели}."
# # pattern = r'[А-яё.\[\]{}-]'
# # print(re.findall(pattern, s1))
#
# # s1 = "Час в 24-часовом формате от 00 до 23. 2021-06-15T 29:59. Минуты, в диапазоне от 00 до 59. 2121-06-15T01:09."
# # pattern = '[0-2][0-9]:[0-5][0-9]'
# # print(re.findall(pattern, s1))
#
# # s1 = "Цифры: 7, +17, -42, 0013, 0.3454564"
# # pattern = r'[+-]?\d+\.?\d*'
# # # pattern = r'[+-]?\d+[.\d]*'
# # print(re.findall(pattern, s1))
#
# # s1 = "05-03-1987 # Дата рождения"
# #
# # print("Дата рождения:", re.sub(r'#[\sА-я]*', '', s1))
# # # print('Дата рождения:', re.sub(r'-?#.*', '.', s1)[:-1])
# # print('Дата рождения:', re.sub(r'-', '.', re.sub(r'#.*', '', s1)))  # "05-03-1987 "
# # # Дата рождения: 05.03.1987
#
# # s1 = "author=Пушкин А.С. title  = Евгений Онегин price =200 year= 1831"
# # # pattern = r'\w+\s*=[^;]+'
# # pattern = r'\w+\s*=\s*\w+\s*[.\w]*'
# # print(re.findall(pattern, s1))
# # print(re.search(pattern, s1))
#
# # s1 = '12 сентября 2021 года 46545463534'
# # reg1 = r'[\d]{,4}'
# # print(re.findall(reg1, s1))
#
# # test = '+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578, 7111111111111'
# # print(re.findall(r'\+?7\d{10}', test))
#
# print(re.findall(reg, s))


# def login(a):
#     return re.findall(r'^[\w!@#$-]{8,25}$', a)
#
#
# a = input('-> ')
# print(login(a))
# print(login('admin!_admin'))

# print(re.findall(r'\w+', '12 + й'))
# print(re.findall(r'\w+', '12 + й', flags=re.ASCII))

# print(re.findall(r'[а-я]', 'Я я', re.IGNORECASE))

# text = """
# one
# two
# """
# print(re.findall(r'^one$', text))
# print(re.findall(r'^one$', text, re.MULTILINE))


# text = """
# one\ntwo
# """
# print(re.findall(r'\d*', text))
# print(re.findall(r'one.\w+', text, re.DOTALL))

# print(re.findall("""
#                     [A-z.-]+   # part 1
#                     @          # поиск символа @
#                     [a-z_.-]+  # part 2
# """, 'test@mail.ru', re.VERBOSE))


# text = 'hello world '
# print(re.findall(r'\w\+', text, re.DEBUG))

# text = """Python,
# python,
# PYTHON"""
# reg = "(?mi)^python"
# print(re.findall(reg, text))  # flags=re.IGNORECASE | re.MULTILINE

# s = "123456@i.ru&, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru0."
#
# reg = r'[\w.-]+@[\w.]+[a-z]{2,3}'
# print(re.findall(reg, s))

# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall("<.+?>", text))

# greedy (жадный)
# lazy (ленивый)

# *?, +?, ??
# {m,n}?, {,n}?, {m,}?

# t = "2324 786 22 4569"
# reg = r'\d{1,3}?'
# print(re.findall(reg, t))

# s = "<p>Изображение <img alt='картинка' src='bg.jpg' title='подсказка'> - фон страницы</p>"
# reg = r'<img\s+[^>]*src\s*=\s*[^>]+>'
# # reg = r'<img[^>]*>'
# print(re.findall(reg, s))  # <img src='bg.jpg'>

# s = "Python (в русском языке встречаются названия питон[16] или пайтон[17]) - высокоуровненый язык программирования " \
#     "общего назначения с динамической строгой типизацией и автоматическим управлением памятью[18][19]."
#
# print(re.findall(r'\[\d+]', s))

# s = 'Петр и Ольга отлично учатся!'
# reg = 'Петр|Пётр|Виталий|Ольга'
# print(re.findall(reg, s))

# s = "int = 4, float = 4.0, double = 8.0f"
# reg = r"(?:int|double)\s*=\s*(?:\d+[.\w+]*)"
# reg = r"int\s*=\s*\d+[.\w+]*|double\s*=\s*\d+[.\w+]*"
# print(re.findall(reg, s))

# () - группирующая скобка
# (?:) - группирующая скобка, не сохраняющая

# 192.168.255.255
# s = '127.0.2.1'
# # reg = r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}'
# reg = r'(?:\d{1,3}.){3}\d{1,3}'
# print(re.findall(reg, s))

# s = "Word2016, PS6, AI5"
# reg = r'(([A-z]+)(\d*))'
# print(re.findall(reg, s))

# s = "5 + 7*2 - 4"
# # reg = r'\s*[+*-]\s*'  # ['5', '7', '2', '4']
# # reg = r'\s*([+*-])\s*'  # ['5', '+', '7', '*', '2', '-', '4']
# reg = r'[^+* -]'  # ['5', '+', '7', '*', '2', '-', '4']
# print(re.split(reg, s))

# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта."
# reg = r'([0-9]+)\s(\D+)'
# print(re.search(reg, s).group())
# m = re.search(reg, s)
# print(m[1])
# print(m[2])
# print(m[0])
# print(re.search(reg, s).group(1))


# text = """
# Самара
# Москва
# Тверь
# Уфа
# Казань
# """
# count = 0
#
#
# def replace_find(m):
#     global count
#     count += 1
#     return f"<option value='{count}'>{m.group(1)}</option>\n"
#
#
# print(re.sub(r"\s*(\w+)\s*", replace_find, text))


# s = "<p>Изображение <img src='bg.jpg'> - фон страницы</p>"
# reg = r'<img\s+[^>]*src=([\'"])(.+)\1>'
# print(re.findall(reg, s))

# s = "<p>Изображение <img src='bg.jpg'> - фон страницы</p>"
# reg = r'<img\s+[^>]*src=(?P<q001>[\'"])(.+)(?P=q001)>'
# print(re.findall(reg, s))

# s = "Самолет прилетает 10/23/2023. Будем рады вас видеть после 10/24/2023."
# reg = r'(\d{2})/(\d{2})/(\d{4})'
# print(re.findall(reg, s))
# print(re.sub(reg, r'\2.\1.\3', s))

# s = "google.com and google.ru and yandex.ru"
# reg = r'(([a-z0-9-]{2,}\.)+[a-z]{2,4})'
# print(re.findall(reg, s))
# print(re.sub(reg, r"http://\1", s))

# Рекурсия

# def elevator(n):
#     if n == 0:
#         print("Вы в подвале")
#         return
#     print("=>", n)
#     elevator(n - 1)   # 5 4 3 2 1
#     print(n, end=" ")
#
#
# n1 = int(input("На каком Вы этаже: "))  # 5
# elevator(n1)

# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res = res + i
#     return res
#
#
# print(sum_list([1, 3, 5, 7, 9]))  # 25

# def sum_list(lst):
#     if len(lst) == 1:
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0]  # 9
#     else:
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0] + sum_list(lst[1:])  # 1 + 3 + 5 + 7 + 9
#
#
# print(sum_list([1, 3, 5, 7, 9]))  # 25


# def to_str(n, base):
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n]  # 15 (F)
#     else:
#         return to_str(n // base, base) + convert[n % base]  # 13 (D)
#
#
# print(to_str(253, 16))  # 253 // 16 = 15

# names = ['Adam', ["Bob", ["Chet", "Cat"], "Bard", "Bert"], 'Alex', ["Bea", "Bill"], 'Ann']

# print(type(names[0]) == str)
# print(type(names[0]) == list)
# print(names[0])
# print(isinstance(names[0], list))
# print(names[1][1])
# print(isinstance(names[1][1], list))
# print(names[1][1][0])
# print(isinstance(names[1][1][0], list))


# names = ['Adam', ["Bob", ["Chet", "Cat"], "Bard", "Bert"], 'Alex', ["Bea", "Bill"], 'Ann']
# # ["Bob", ["Chet", "Cat"], "Bard", "Bert"]
# # ["Chet", "Cat"]
#
#
# def count(lst):
#     cnt = 0
#     for i in lst:
#         if isinstance(i, list):
#             cnt += count(i)
#         else:
#             cnt += 1
#     return cnt  # (10)
#
#
# print(count(names))


# names = ['Adam', ["Bob", ["Chet", "Cat"], "Bard", "Bert"], 'Alex', ["Bea", "Bill"], 'Ann']
# # [["Bob", ["Chet", "Cat"], "Bard", "Bert"], 'Alex', ["Bea", "Bill"], 'Ann']
#
#
# def union(s):
#     if not s:  # s == [] - список пустой
#         return s
#     if isinstance(s[0], list):
#         return union(s[0]) + union(s[1:])
#     return s[:1] + union(s[1:])  # 'Adam' "Bob" "Chet" "Cat"
#
#
# print("Выпрямленный список:", union(names))
# print(names)


# def remove(text):
#     if not text:
#         return ""
#     if text[0] == "!" or text[0] == "&":
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])   # HelloWorld
#
#
# print(remove("&Hello!World"))


# def list_merge(lst):
#     merge = []
#     while lst:
#         i = lst.pop(0)
#         if isinstance(i, list):
#             lst = i + lst
#         else:
#             merge.append(i)
#     return merge
#
#
# ls = ['Adam', ['Bob', ['Chet', 'Cat'], 'Bard', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
#
# print(list_merge(ls))

# import re
#
# str1 = '1X, TEXT ABC 724 A1B2C3'
# num_1 = re.findall(r"^(\d)[A-z]", str1)
# num_2 = re.findall(r"[A-z](\d)", str1)
# print(num_1 + num_2)
# # reg1 = r'(\d)[A-z]|(\d)$'
# # print(re.findall(reg1, str1))
#
#
# str2 = 'text from #START# till #END#'
# reg2 = r''
# print(re.findall(reg2, str2))
#
#
# str3 = '12_34__56_5'
# reg3 = r'(\d+)_[^_]'
# print(re.findall(reg3, str3))

# def func(n):
#     if len(n) == 0:  # n == [] подчеркивает , но можно поставить - not n (наведя на подчеркивание)
#         return 0  # len(n)
#     elif n[0] < 0:
#         return 1 + func(n[1:])
#     else:
#         return func(n[1:])
#
#
# print('n =', func([-2, 3, 8, -11, -4, 6]))

# def func(n):  # [-2, 3, 8, -11, -4, 6]
#     if not n:  # len(n) == 0 || n == []
#         return 0  # len(n)
#     else:
#         res = func(n[1:])
#         # [-2, 3, 8, -11, -4, 6]
#         # [3, 8, -11, -4, 6]
#         # [8, -11, -4, 6]
#         # [-11, -4, 6]
#         # [-4, 6]
#         # [6]
#         if n[0] < 0:
#             res += 1  # 1 + 1 + 1    # return func(n[1:]) + 1 - не работает вместо второстепенной переменной
#         print(res)
#         return res
#
#
# print('n =', func([-2, 3, 8, -11, -4, 6]))

# Файлы

# f = open('D:\\Python228\\text.txt', 'r')
# f = open('text.txt')
# # print(f)
# # print(*f)
# f.close()
# print(f.closed)
# print(f.mode)
# print(f.name)
# print(f.encoding)

# f = open('text.txt', 'r')
# print(f.read(3))
# print(f.read())
# f.close()

# f = open('text.txt', 'r')
# try:
#     print(f.read())
# finally:
#     f.close()


# f = open('test.txt', 'r')
# print(f.readline())
# print(f.readline(8))
# print(f.readline())
# print(f.readline())
# f.close()

# f = open('test.txt', 'r')
# print(f.readlines(20))
# f.close()
#
# f = open('test.txt', 'r')
# for line in f:
#     print(line, end='\r')
# f.close()

# f = open('test.txt', 'r')
# count = 0
# for line in f:
#     count += 1
# f.close()
# print(count)
#
# f = open('test.txt', 'r')
# print(f.readlines(3))
# cnt = len(f.readlines())
# f.close()
# print(cnt)

# f = open('xyz.txt', 'w')
# f.write('Привет\nМир!')
# f.close()
#
# f = open('xyz.txt', 'a')
# # print(f.write('\nНовый текст'))
# lines = ['\nЛиния 1', '\nЛиния 2']
# f.writelines(lines)
# f.close()


# f = open('xyz.txt', 'w')
# lst = [str(i) + str(i-1) for i in range(1, 20)]
# print(lst)
# # f.writelines(lst)
# for index in lst:
#     f.write(index + '\t')
# f.close()


# f = open("text2.txt", "w")
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл")
# f.close()

# f = open("text2.txt", "r")
# read_file = f.readlines()
# print(read_file)
# for i in range(len(read_file)):
#     if read_file[i] == 'изменить строку в списке;\n':
#         read_file[i] = 'Hello world!\n'
# print(read_file)
# f.close()
#
# f = open("text2.txt", "w")
# f.writelines(read_file)
# f.close()

# f = open("text2.txt", "w")
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл")
# f.close()

# f = open('text3.txt', 'w')
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл")
# f.close()
#
#
# f = open('text3.txt', 'r')
# read_line = f.readlines()
# print(read_line)
# n = int(input("Введите индекс: "))
#
# if 0 <= n < len(read_line):
#     read_line.pop(n)
# else:
#     print('Такой строки нет')
# print(read_line)
# f.close()
#
# f = open('text3.txt', 'w')
# f.writelines(read_line)
# f.close()


# f = open('text.txt', 'r')
# print(f.read(3))
# print(f.tell())
# print(f.seek(1))
# print(f.read())
# print(f.tell())
# f.close()


# f = open('text4.rtf', 'wb')
# print(f.write(b"\nI am learning Python\n"))  # 20
# # print(f.seek(3))  # 3
# # print(f.write("--new string--"))  # 14
# # print(f.tell())  # 17
# f.close()


# with open('text5.txt', 'w+') as f:
#     print(f.write('0123456789'))

# with open('text2.txt', 'r') as f:
#     for line in f:
#         print(line[:6])

# file_name = 'res.txt'
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]


# def get_line(lt):
#     lt = list(map(str, lt))
#     return ' '.join(lt)  # lt ['4.5', '2.8', '3.9', '1.0', '0.3', '4.33', '7.777']
#
#
# with open(file_name, 'w') as f:
#     f.write(get_line(lst))
# print(get_line(lst))

# with open(file_name, 'r') as f:
#     nums = f.read()
#
# print(nums)
#
# lst = list(map(float, nums.split(' ')))
# print(lst)
# print(len(lst))
# print(sum(lst))


# def longest_words(file):
#     with open(file, 'r') as text:
#         w = text.read().split()
#         max_length = len(max(w, key=len))
#         res = [word for word in w if len(word) == max_length]
#         if len(res) == 1:
#             return res[0]
#         return res
#
#
# file_name = 'res.txt'
# print(longest_words(file_name))

# text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10\n"
#
# with open("one.txt", 'w') as f:
#     f.write(text)

# read_file = 'one.txt'
# write_file = 'two.txt'
# with open(read_file, 'r') as fr, open(write_file, 'w') as fw:
#     for line in fr:
#         line = line.replace("Строка", "Линия - ")
#         fw.write(line)


# Модуль OS и OS.PATH

# import os
# import os.path

# print("Текущая директория: ", os.getcwd())  # D:\Python228
#
# print(os.listdir(".."))  # возвращает список директорий и файлов, находящихся в текущей директории
# os.mkdir("folder")  # создает директорию по указанному пути
# os.makedirs("nested1/nested5/nested3")  # создает промежуточные директории и конечную, указанные в пути, если они не
# # существуют. Если конечная директория уже существует, то будет сгенерирована ошибка FileExistsError

# os.remove("xyz.txt")  # удаление файла

# os.rename('nested1', 'test')  # переименовывает файл или директорию
# os.rename('test.txt', 'test/test1.txt')  # переименовывает файл или директорию, перемещает файлы в сущестующие
# директории (переместил файл)
# os.renames('text.txt', 'test1/test1.txt')  # переименовывает файл или директорию, создавая промежуточные директории (
# переместил файл)

# os.rmdir("test1")  # удаляет пустую директорию

# for root, dirs, files in os.walk('test', topdown=False):  # возвращает имена объектов в виде дерева директорий. Для
#     # каждой директории возвращает кортеж (root - путь к директории, dirs - список директорий, files - список файлов)
#     print("Root:", root)
#     print("   Subdirs:", dirs)
#     print("   Files:", files)


# def remove_empty_dirs(root_tree):
#     for root, dirs, files in os.walk(root_tree):
#         if not os.listdir(root):
#             os.rmdir(root)
#             print(f"Директория {root} удалена.")
#
#
# remove_empty_dirs('test')


# print(os.path.split(r"D:\Python228\test\nested5\test1.txt"))  # разбивает путь на кортеж (head, tail),
# # tail - последний компонент пути, head - все остальное
#
# print(os.path.dirname(r"D:\Python228\test\nested5\test1.txt"))  # возвращает имя директории (+ путь)
# print(os.path.basename(r"D:\Python228\test\nested5\test1.txt"))  # возвращает имя файла

# print(os.path.join('files', 'pythonProject1', 'dir', 'three.txt'))


# dirs = ["Work/F1", "Work/F2/F21"]
#
# for d in dirs:
#     os.makedirs(d)

# files = {'Work': ['w.txt'],
#          'Work/F1': ['f11.txt', 'f12.txt', 'f13.txt'],
#          'Work/F2/F21': ['f211.txt', 'f212.txt']
#          }
#
# for d, file in files.items():
#     for f in file:
#         file_path = os.path.join(d, f)
#         open(file_path, 'w').close()
#
#
# file_text = ['Work/w.txt', 'Work/F1/f12.txt', 'Work/F2/F21/f211.txt', 'Work/F2/F21/f212.txt']
# for file in file_text:
#     with open(file, 'w') as f:
#         f.write(f"Текст для файла по пути {file}.")
#
#
# def print_tree(root, td):
#     print(f'Обход {root} {"сверху вниз" if td else "снизу вверх"}')
#     for root, dirs, fl in os.walk(root, topdown=td):
#         print(root)
#         print(dirs)
#         print(fl)
#     print("-" * 50)
#
#
# print_tree('Work', td=False)
# print_tree('Work', td=True)

# print(os.path.exists(r'Work\w.txt'))  # проверяет наличие файла или папки по указанному пути

# import time
#
# path = 'git.txt'
# # print(os.path.getatime(path))  # возвращает время последнего доступа к файлу в секундах
# # print(os.path.getctime(path))  # возвращает время создания файла
# # print(os.path.getmtime(path))  # возвращает время последнего изменения файла
# # print(os.path.getsize(path))  # размер файла в байтах
#
# size = round(os.path.getsize(path) / 1024, 2)
# print(size)
# t = os.path.getctime(path)
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(t)))

# print(os.path.isfile(r'Work\w.txt'))  # возвращает True, если путь является файлом
# print(os.path.isdir(r'Work'))  # возвращает True, если путь является директорией

# class Point:
#     """Класс для представления координат точек на плоскости"""
#     x = 1
#     y = 1
#
# # print(Point.__doc__)
# # print(Point.__name__)
# # print(dir(Point))
#
# x = 5
# p1 = Point()
# p2 = Point()
# print("p1 =", p1.x)
# print("p2 =", p2.x)
# print("Point =", Point.x)
# print(type(p1))
# p1.x = 100
# p2.x = 200
# print("p1 =", p1.x)
# print("p2 =", p2.x)
# print("Point =", Point.x)
# print(id(p1))
# print(id(p2))
# print(id(Point))
# Point.y = 300
# Point.x = 400
# print("p1 =", p1.y)
# print("p2 =", p2.y)
# print("Point =", Point.y)
# print("p1 =", p1.x)
# print("p2 =", p2.x)
# print("Point =", Point.x)


# class Point:
#     x = 1
#     y = 1
#     c = 2
#
#
# p1 = Point()
#
# # p1.x = 5
# # p1.y = 10
# # p1.z = 20
# Point.z = 50
# print(p1.x, p1.y, p1.c)
# print(p1.__dict__)
# print(Point.__dict__)


# class Point:
#     x = 1
#     y = 1
#
#     def set_coord(self):
#         print(self.__dict__)
#
#
# p1 = Point()
# print(p1.x)
# p1.x = 5
# p1.y = 10
# p1.set_coord()
# Point.set_coord(p1)
# p2 = Point()
# p2.x = 2
# p2.y = 7
# p2.set_coord()


# class Point:
#     x = 1
#     y = 1
#
#     def set_coord(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point()
# p1.set_coord(5, 10)
# print(p1.__dict__)
# print(p1.x)
# p2 = Point()
# p2.set_coord(2, 7)
# print(p2.__dict__)
# print(p2.x)
# Point.set_coord(p2, 5, 8)
# print(p2.__dict__)


# class Human:
#     name = 'name'
#     birthday = '00.00.0000'
#     phone = '00-00-00'
#     country = 'country'
#     city = 'city'
#     address = 'street, house'
#
#     def print_info(self):
#         print(" Персональные данные ".center(40, "*"))
#         print(f"Имя: {self.name}\nДата рождения: {self.birthday}\nНомер телефона: {self.phone}\n"
#               f"Страна: {self.country}\nГород: {self.city}\nДомашний адрес: {self.address}")
#         print("=" * 40)
#
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.name = first_name
#         self.birthday = birthday
#         self.country = country
#         self.phone = phone
#         self.city = city
#         self.address = address
#
#     def set_name(self, name):  # установить имя
#         if isinstance(name, str):
#             self.name = name
#
#     def get_name(self):  # получить имя
#         return self.name
#
#     def set_birthday(self, bth):
#         self.birthday = bth
#
#     def get_birthday(self):
#         return self.birthday
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info("Юля", '23.05.1986', '45-46-98', 'Россия', 'Москва', 'Чистопрудный бульвар, 1А')
# h1.print_info()
# h1.set_name("Алевтина")
# h1.print_info()
# print(h1.get_name())
# h1.set_birthday('23.01.1987')
# print(h1.get_birthday())

# class Person:
#     skill = 10
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def print_info(self):
#         print("Данные сотрудника:", self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print("Квалификация сотрудника:", self.skill, "\n")
#
#
# p1 = Person("Viktor", "Reznik")
# p1.print_info()
# p1.add_skill(3)
#
# p2 = Person("Anna", "Dolgih")
# p2.print_info()
# p2.add_skill(2)

# class Point:
#     # def __new__(cls, *args, **kwargs):
#     #     print("Конструктор")
#     #     return super().__new__(cls)
#
#     def __init__(self, x, y):
#         print("Инициализатор")
#         self.x = x
#         self.y = y
#
#     def __del__(self):
#         print("Удаление экземпляра", self.__class__.__name__)
#
#     def print_coord(self):
#         print(f"x: {self.x}, y: {self.y}")
#
#
# p1 = Point(5, 10)
# p1.print_coord()
# print(id(p1))
#
# p2 = Point(2, 7)
# p2.print_coord()
# print(id(p2))


# class Point:
#     count = 0
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         Point.count += 1
#
#
# p1 = Point(5, 10)
#
#
# p2 = Point(7, 2)
# # print(p2.count)

# p3 = Point(3, 4)
# print(p3.count)
# print("->", Point.count)
# print(p1.count)
#
# print(id(p1.count))
# print(id(p2.count))
# print(id(p3.count))
# print(id(Point.count))


# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print("Инициализация робота:", self.name)
#         Robot.k += 1
#
#     def __del__(self):
#         print(self.name, "выключается!")
#         Robot.k -= 1
#
#         if Robot.k == 0:
#             print(self.name, "был последним")
#         else:
#             print("Работающих роботов осталось:", Robot.k)
#
#     def say_hi(self):
#         print("Приветствую. Меня зовут", self.name)
#
#
# droid1 = Robot("R2-D2")
# droid1.say_hi()
# print("Численность роботов:", Robot.k)
#
# droid2 = Robot("C-3PO")
# droid2.say_hi()
# print("Численность роботов:", Robot.k)
#
# droid3 = Robot("RP-O")
# droid3.say_hi()
# print("Численность роботов:", Robot.k)
#
# print("\nЗдесь роботы могут проделать какую-то работу\n")
# print("Роботы закончили свою работу. Давайте их выключим")
# del droid1
# del droid2
# del droid3
# print("Численность роботов в конце программы:", Robot.k)


# class Point:
#     __slots__ = ["__x", "__y", "z"]
#
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x  # _Point__x
#             self.__y = y
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coord(self, x, y):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def set_coord_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Координаты должны быть числами")
#
#     def set_coord_y(self, y):
#         if Point.__check_value(y):
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_coord(self):
#         return self.__x, self.__y
#
#     def get_coord_x(self):
#         return self.__x
#
#     def get_coord_y(self):
#         return self.__y
#
#
# p1 = Point(5, 10)
# p1.z = 15
# print(p1.z)
# print(p1.__dict__)
# print(p1._Point__x)
# p1._Point__x = 111
# print(p1.get_coord())
# p1.set_coord(1, 2.3)
# print(p1.get_coord())
# print(p1.__dict__)
# p1.set_coord_x(8)
# print(p1.get_coord_x())
# p1.set_coord_y(9)
# print(p1.get_coord_y())
# # p1.__x = 100
# # p1.__y = 'abc'
# # print(p1.__x, p1.__y)
# print(p1.__dict__)


# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __set_x(self, x):  # устанавливаем
#         print("Вызов __set_x")
#         self.__x = x
#
#     def __get_x(self):  # получаем
#         print("Вызов __get_x")
#         return self.__x
#
#     def __del_x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     x = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# p1.x = 100
# print(p1.__dict__)
# print(p1.x)
# del p1.x


# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     @property
#     def x(self):  # получаем  __get_x
#         print("Вызов __get_x")
#         return self.__x
#
#     @x.setter
#     def x(self, x):  # устанавливаем __set_x
#         print("Вызов __set_x")
#         self.__x = x
#
#     @x.deleter
#     def x(self):  # __del_x
#         print("Удаление свойства")
#         del self.__x
#
#     # x = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# p1.x = 100
# # print(p1.__dict__)
# print(p1.x)
# del p1.x

# class KgToPounds:
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.setter
#     def kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             print('Килограммы задаются только числами')
#
#     def to_pounds(self):
#         return self.__kg * 2.205
#
#
# weight = KgToPounds(12)
# print(weight.kg, "кг =>", end=" ")
# print(weight.to_pounds(), 'фунтов')
# weight.kg = 41
# print(weight.kg, "кг =>", end=" ")
# print(weight.to_pounds(), 'фунтов')
# weight.kg = 'десять'


# class Point:
#     __count = 0
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         Point.__count += 1
#
#     @staticmethod
#     def get_count():
#         return Point.__count
#
#     # get_count = staticmethod(get_count)
#
#
# p1 = Point(5, 10)
# p2 = Point(4, 8)
# p3 = Point(2, 7)
# print(Point.get_count())
# print(p1.get_count())
# # Point.set_coord(p1)


# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
#
# c1 = Change()
# print(Change.inc(10), Change.dec(10))
# print(c1.inc(10), c1.dec(10))
#
#
# def inc(x):
#     return x + 1

#
# def dec(x):
#     return x - 1
#
#
# print(inc(10), dec(10))


# class Numbers:
# @staticmethod
# def max(*args):
#     print(args)
#     max1 = 0
#     for i in args:
#         max1 = max1 if i < max1 else i
#     return max1
#     @staticmethod
#     def max(*args):
#         res = args[0]
#         for i in args:
#             if i > res:
#                 res = i
#         return res
#
#
# print(Numbers.max(3, 5, 7, 9, 4, 16, 1))


# class Date:
#
#     def __init__(self, day=0, month=0, year=0):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     def __str__(self):
#         return f"{self.day}, {self.month}, {self.year}"
#
#     @classmethod
#     def from_string(cls, date_as_string):
#         day1, month1, year1 = map(int, date_as_string.split('.'))
#         # print(cls(day, month, year))
#         return cls(day1, month1, year1)
#
#     def string_to_db(self):
#         return f"{self.year}-{self.month}-{self.day}"


# d = Date(11, 11, 1111)
# print(d)
# print(d.string_to_db())
# string_date = Date.from_string('23.10.2022')
# print(string_date)  # (23, 10, 2022)
# print(Date.string_to_db(string_date))
# print(string_date.string_to_db())
# string_date1 = Date.from_string('21.12.2021')
# print(string_date1.string_to_db())

# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = "RUB"
#     suffix_usd = "USD"
#     suffix_eur = 'EUR'
#
#     def __init__(self, num, surname, percent, value=0):
#         self.num = num
#         self.surname = surname
#         self.percent = percent
#         self.value = value
#         print(f"Счет #{self.num} принадлежащий {self.surname} был открыт.")
#         print("*" * 50)
#
#     def __del__(self):
#         print("*" * 50)
#         print(f"Счет #{self.num} принадлежащий {self.surname} был закрыт.")
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def add_percents(self):
#         self.value += self.value * self.percent
#         print('Проценты были успешно начислены!')
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f"К сожалению у вас нет {val} {Account.suffix}")
#         else:
#             self.value -= val
#             print(f'{val} {Account.suffix} было успешно снято!')
#         self.print_balance()
#
#     def add_money(self, val):
#         self.value += val
#         print(f'{val} {Account.suffix} было успешно добавлено!')
#         self.print_balance()
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f'Состояние счета: {usd_val} {Account.suffix_usd}')
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.value, Account.rate_eur)
#         print(f'Состояние счета: {eur_val} {Account.suffix_eur}')
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.value} {Account.suffix}")
#
#     def print_info(self):
#         print('Информация о счете')
#         print("-" * 20)
#         print(f"#{self.num}")
#         print(f'Владелец: {self.surname}')
#         self.print_balance()
#         print(f"Проценты: {self.percent:.0%}")
#         print("-" * 20)
#
#
# acc = Account('12345', 'Долгих', 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# Account.set_usd_rate(2)
# acc.convert_to_usd()
# Account.set_eur_rate(3)
# acc.convert_to_eur()
# print()
# acc.edit_owner("Дюма")
# acc.print_info()
# print()
# acc.add_percents()
# print()
# acc.withdraw_money(3000)
# print()
# acc.withdraw_money(100)
# print()
# acc.add_money(5000)
# print()
# acc.withdraw_money(3000)
# print()

# import re
#
#
# class UserData:
#     def __init__(self, fio, old, ps, weight):
#         self.fio = fio
#         self.old = old
#         self.password = ps
#         self.weight = weight
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, year):
#         self.verify_old(year)
#         self.__old = year
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, weight):
#         self.verify_weight(weight)
#         self.__weight = weight
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, ps):
#         self.verify_ps(ps)
#         self.__password = ps
#
#     @staticmethod
#     def verify_fio(fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО должно быть строкой")
#         f = fio.split()  # ['Волков', 'Игорь', 'Николаевич']
#         if len(f) != 3:
#             raise TypeError("Неверный формат ФИО")
#         # ['В', 'о', 'л', 'к', 'о', 'в', 'И',
#         # 'г', 'о', 'р', 'ь', 'Н', 'и', 'к', 'о', 'л', 'а', 'е', 'в', 'и', 'ч']
#         letters = "".join(re.findall('[a-zа-яё-]', fio, flags=re.IGNORECASE))  # ВолковИгорьНиколаевич
#         for s in f:
#             if len(s.strip(letters)) != 0:
#                 raise TypeError("В ФИО можно использовать только буквы и дефис")
#
#     @staticmethod
#     def verify_old(old):
#         if not isinstance(old, int) or not 14 < old < 120:  # old < 14 or old > 120
#             raise TypeError("Возраст должен быть числом в диапазоне от 14 до 120 лет")
#
#     @staticmethod
#     def verify_weight(w):
#         if not isinstance(w, float) or w < 20:
#             raise TypeError("Вес должен быть вещественным числом от 20 кг и выше")
#
#     @staticmethod
#     def verify_ps(ps):
#         if not isinstance(ps, str):
#             raise TypeError("Паспорт должен быть строкой")
#         s = ps.split()  # ['1234', '567890']
#         # print(s)
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError("Неверный формат паспорта")
#         for p in s:
#             if not p.isdigit():
#                 raise TypeError("Серия и номер паспорта должны быть числами")
#
#
# p1 = UserData("Волков Игорь Николаевич", 26, "1234 567890", 80.8)
# p1.fio = "Сидоров Игорь Николаевич"
# print(p1.fio)
# print(p1.__dict__)


# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         print("Инициализатор базового класса")
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self.__width = width
#
#     def get_width(self):
#         return self.__width
#
#
# class Line(Prop):
#     def __init__(self, *args):
#         print("Переопределенный инициализатор Line")
#         # Prop.__init__(self, *args)
#         super().__init__(*args)
#
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self.get_width()}")
#
#
# class Rect(Prop):
#     def __init__(self, *args, bg="yellow"):
#         super().__init__(*args)
#         self._background = bg
#
#     def draw_rect(self):
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self.get_width()}, {self._background}")
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# Line.draw_line(line)
# rect = Rect(Point(30, 40), Point(70, 80))
# rect.draw_rect()

# DRY (Don't Repeat Yourself) - не повторяйся!!!

# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     def __str__(self):
#         return f"{self.__color}"
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
#
# class Rectangle(Figure):
#     def __init__(self, width, height, color):
#         super().__init__(color)
#         self.width = width
#         self.height = height
#
#     def __str__(self):
#         return f"{self.__width}, {self.__height}, {self.color}"
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, w):
#         if w > 0:
#             self.__width = w
#         else:
#             raise ValueError("Ширина должна быть положительное число")
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, h):
#         if h > 0:
#             self.__height = h
#         else:
#             raise ValueError("Высота должна быть положительное число")
#
#     def area(self):
#         return self.width * self.height
#
#
# rect = Rectangle(10, 20, 'green')
# print(rect)
# print(rect.width)
# print(rect.height)
# print(rect.color)
# rect.color = "red"
# rect.width = 5
# print(rect)
# print(rect.area())


# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def show_rect(self):
#         print(f"=== Прямоугольник ===\nШирина: {self.width}\nВысота: {self.height}")
#
#
# class RectFon(Rect):
#     def __init__(self, width, height, background):
#         self.fon = background
#         super().__init__(width, height)
#
#     def show_rect(self):
#         super().show_rect()
#         print("Фон:", self.fon)
#
#
# class RectFonBorder(RectFon):
#     def __init__(self, width, height, background, border):
#         super().__init__(width, height, background)
#         self.border = border
#
#     def show_rect(self):
#         super().show_rect()
#         print('Рамка:', self.border)
#
#
# class RectBorder(Rect):
#     def __init__(self, width, height, border):
#         self.border = border
#         super().__init__(width, height)
#
#     def show_rect(self):
#         super().show_rect()
#         print('Рамка:', self.border)
#
#
# shape = Rect(100, 200)
# shape.show_rect()
# print()
# shape1 = RectFon(400, 300, 'yellow')
# shape1.show_rect()
# print()
# shape2 = RectBorder(600, 500, '1px solid red')
# shape2.show_rect()
# print()
# shape3 = RectFonBorder(600, 500, "yellow", '1px solid red')
# shape3.show_rect()

# class Vector(list):
#     def __str__(self):
#         return " ".join(map(str, self))  # 1 2 3
#
#
# v = Vector([1, 2, 3])
# print(v)
# print(type(v))

# Перегрузка методов


# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_int(self):
#         if not isinstance(self.__x, int) or not isinstance(self.__y, int):
#             print("Координаты должны быть целочисленными")
#             return False
#         return True
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#
# class Line(Prop):
#
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#     def set_coord(self, sp, ep=None):
#         if ep is None:
#             if sp.is_int():
#                 self._sp = sp
#         else:
#             if sp.is_int() and ep.is_int():
#                 self._sp = sp
#                 self._ep = ep
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coord(Point(20, 40), Point(50, 60))
# line.draw_line()
# line.set_coord(Point(100, 240))
# line.draw_line()


# Абстрактные методы

# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_int(self):
#         if not isinstance(self.__x, int) or not isinstance(self.__y, int):
#             print("Координаты должны быть целочисленными")
#             return False
#         return True
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def draw_line(self):
#         raise NotImplementedError("В дочернем классе должен быть определен метод draw()")
#
#
# class Line(Prop):
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#     pass
#
#
# line = Line(Point(1, 2), Point(10, 20), width=2)
# line.draw_line()
# from math import pi
#
#
# class Table:
#     def __init__(self, width=None, length=None, radius=None):  # radius=20
#         if radius is None:
#             if length is None:
#                 self._width = self._length = width
#             else:
#                 self._width = width
#                 self._length = length
#         else:
#             self._radius = radius
#
#     def calc_area(self):
#         raise NotImplementedError("В дочернем классе должен быть определен метод calc_area()")
#
#
# class SqTable(Table):
#     def calc_area(self):
#         return self._width * self._length
#
#
# class RoundTable(Table):
#     def calc_area(self):
#         return round(pi * self._radius ** 2, 2)
#
#
# tt = Table()

# t = SqTable(20, 10)
# print(t.__dict__)
# print(t.calc_area())
#
# t2 = SqTable(20)
# print(t2.__dict__)
# print(t2.calc_area())
#
# t1 = RoundTable(radius=20)
# print(t1.__dict__)
# print(t1.calc_area())


# from abc import ABC, abstractmethod
#
#
# class Chess(ABC):
#     def draw(self):
#         print("Нарисовал шахматную фигуру")
#
#     @abstractmethod
#     def move(self):
#         print("Родитель")
#
#
# class Queen(Chess):
#     # def move(self):
#     #     super().move()
#     #     print("Переместил шахматную фигуру")
#     ...
#
#
# q = Queen()
# q.draw()
# # q.move()


# from abc import ABC, abstractmethod
#
#
# class Currency(ABC):
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     def print_value(self):
#         print(self.value, end=" ")
#
#
# class Dollar(Currency):
#     rate_to_rub = 74.16
#     suffix = 'USD'
#
#     def convert_to_rub(self):
#         rub = self.value * Dollar.rate_to_rub
#         return rub
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, end=" ")
#
#
# class EUR(Currency):
#     rate_to_rub = 90.14
#     suffix = 'EUR'
#
#     def convert_to_rub(self):
#         rub = self.value * EUR.rate_to_rub
#         return rub
#
#     def print_value(self):
#         super().print_value()
#         print(EUR.suffix, end=" ")
#
#
# d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# print("*" * 50)
# for elem in d:
#     elem.print_value()
#     print(f'= {elem.convert_to_rub():.2f} RUB')
#
# print("*" * 50)
# e = [EUR(5), EUR(10), EUR(50), EUR(100)]
# for elem in e:
#     elem.print_value()
#     print(f"= {elem.convert_to_rub():.2f} RUB")


# from abc import ABC, abstractmethod
#
#
# class Father(ABC):
#     @abstractmethod
#     def display1(self):
#         pass
#
#     @abstractmethod
#     def display2(self):
#         pass
#
#
# class Child(Father):
#     def display1(self):
#         print("Дочерний класс")
#
#
# class GrandChild(Child):
#     def display2(self):
#         print("Внучатый класс")
#
#
# gc = GrandChild()
# gc.display2()
# gc.display1()


# Вложенные классы

# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def outer_class_method():
#         print("Я - метод внешнего класса")
#
#     def outer_obj_method(self):
#         print("Связующий метод")
#
#     class MyInner:
#         def __init__(self, inner_name, obj):
#             self.inner_name = inner_name
#             self.obj = obj
#
#         def inner_method(self):
#             print("Я - метод вложенного класса", MyOuter.age, self.obj.name)
#             MyOuter.outer_class_method()
#             self.obj.outer_obj_method()
#
#
# out = MyOuter('внешний')
# inner = out.MyInner("внутренний", out)
# print(inner.inner_name)
# inner.inner_method()

# class Color:
#     def __init__(self):
#         self.name = "Green"
#         self.lg = self.LightGreen()
#
#     def show(self):
#         print("Name:", self.name)
#
#     class LightGreen:
#         def __init__(self):
#             self.name = "Light green"
#             self.code = '024avc'
#
#         def display(self):
#             print("Name:", self.name)
#             print("Code:", self.code)
#
#
# outer = Color()
# outer.show()

# g = outer.lg
# outer.lg.name = "Red"
# outer.lg.display()

# class Intern:
#     def __init__(self):
#         self.name = "Smith"
#         self.id = '657'
#
#     def display(self):
#         print('Name:', self.name)
#         print('Id:', self.id)
#
#
# class Employee:
#     def __init__(self):
#         self.name = "Employee"
#         self.intern = Intern()
#         self.head = self.Head()
#
#     def show(self):
#         print('Name:', self.name)
#
#     class Head:
#         def __init__(self):
#             self.name = "Alba"
#             self.id = '007'
#
#         def display(self):
#             print('Name:', self.name)
#             print('Id:', self.id)
#
#
# outer = Employee()
# outer.show()
#
# d1 = outer.intern
# print()
# d1.display()
# print(d1.id)
# print()
# d2 = outer.head
# d2.display()

# class Computer:
#     def __init__(self, name, os1, brand):
#         self.name = name
#         self.os = self.OS(os1)
#         self.cpu = self.CPU(brand)
#
#     class OS:
#         def __init__(self, title):
#             self.title = title
#
#         def system(self):
#             return self.title
#
#     class CPU:
#         def __init__(self, brand):
#             self.brand = brand
#
#         def make(self):
#             return self.brand
#
#         def model(self, model):
#             return model
#
#
# comp = Computer("PC001", "Windows-7", "Intel")
# my_os = comp.os
# my_cpu = comp.cpu
# print(comp.name)
# print(my_os.system())
# print(my_cpu.make())
# print(my_cpu.model('Core-i7'))
# print(my_cpu.model('Core-i5'))


# class Base:
#     def __init__(self):
#         self.db = self.Inner()
#
#     def display(self):
#         print("In Base Class")
#
#     class Inner:
#         def display1(self):
#             print("Inner of Base Class")
#
#
# class SubClass(Base):
#     def __init__(self):
#         print('In SubClass')
#         super().__init__()
#
#     class Inner(Base.Inner):
#         def display2(self):
#             print("Inner of SubClass")
#
#
# a = SubClass()
# a.display()
#
# # b = a.db
# b = SubClass.Inner()
# b.display1()
# b.display2()

# Множественное наследование

# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name + " is sleeping")
#
#
# class Pet(Creature):
#     def play(self):
#         print(self.name + " is playing")
#
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name + " is barking")
#
#
# beast = Dog("Buddy")
# beast.bark()
# beast.play()
# beast.sleep()

# class A:
#     # def __init__(self):
#     #     print("A")
#     pass
#
#
# class AA:
#     pass
#
#
# class B(A):
#     # def __init__(self):
#     #     print("B")
#
#     def hi(self):
#         print('B_hi')
#
#
# class C(AA):
#     # def __init__(self):
#     #     print("C")
#
#     def hi(self):
#         print('C_hi')
#
#
# class D(B, C):
#     # def __init__(self):
#     #     B.__init__(self)
#     #     C.__init__(self)
#     #     print("D")
#
#     def hi(self):
#         C.hi(self)
#         print('D_hi')
#
#
# d = D()
# # d.hi()
# print(D.mro())
# # print(D.__mro__)


# class B:
#     def hi(self):
#         print('B_hi')
#
#
# class C:
#     def hi(self):
#         print('C_hi')
#
#
# class D(B, C):
#     def hi(self):
#         C.hi(self)
#         print('D_hi')
#
#
# d = D()
# # d.hi()
# print(D.mro())
# class AA:
#     pass
#
# class A(AA):
#     pass

# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#
# class Style:
#     def __init__(self, color="red", width=1):
#         print("Инициализатор Style")
#         self._color = color
#         self._width = width
#
#
# class Pos:
#     def __init__(self, sp: Point, ep: Point, *args):
#         print("Инициализатор Pos")
#         self._sp = sp
#         self._ep = ep
#         super().__init__(*args)
#
#
# class Line(Pos, Style):
#     # def __init__(self, sp, ep, color, width):
#     #     Pos.__init__(self, sp, ep)
#     #     Style.__init__(self, color, width)
#
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# l1 = Line(Point(10, 10), Point(100, 100), 'green', 5)
# l1.draw()
# print(Line.mro())
# print(Point.mro())


# Миксин (примеси)

# class Displayer:
#     @staticmethod
#     def display(message):
#         print(message)
#
#
# class LoggerMixin:
#     def log(self, message, filename='logfile.txt'):
#         with open(filename, 'a') as fh:
#             fh.write(message)
#
#     def display(self, message):
#         Displayer.display(message)
#         self.log(message)
#
#
# class MySubClass(LoggerMixin, Displayer):
#     def log(self, message, filename=""):
#         super().log(message, "subclasslog.txt")
#
#
# sub = MySubClass()
# sub.display("Строка будет отображаться и регистрироваться в файле")
# print(MySubClass.mro())


# Прочитать урок 9 (Объектно-ориентированное программирование) и 10 (Наследование. Исключения)
# В журнале после прочтения написать "прочитал(а)". По желанию можно поделиться впечатлениями о прочитанном


# class Goods:
#     def __init__(self, name, weight, price):
#         # super().__init__(name, weight, price)
#         print("Init Goods")
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def print_info(self):
#         print(f"{self.name}, {self.weight}, {self.price}")
#
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self, name, weight, price):
#         super().__init__(name, weight, price)
#         print("Init MixinLog")
#         MixinLog.ID += 1
#         self.id = self.ID
#         self.goods = Goods(name, weight, price)
#
#     def save_sell_log(self):
#         print(f"{self.id}: товар был продан в 00:00 часов {self.goods.name}")
#
#
# class NoteBook(MixinLog, Goods):
#     pass
#
#
# n = NoteBook('HP', 1.5, 35000)
# # n1 = NoteBook('HP', 1.5, 35000)
# n.print_info()
# n.save_sell_log()
# # n1.save_sell_log()
# print(NoteBook.mro())


# Перегрузка операторов

# 24 * 60 * 60 = 86400 (число секунд в одном дне)

# class Clock:
#     DAY = 86400
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#
#         self.sec = sec % self.DAY
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f"{Clock.get_form(h)}:{Clock.get_form(m)}:{Clock.get_form(s)}"
#
#     @staticmethod
#     def get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.sec + other.sec)
#
#     # def __mul__(self, other):
#     #     if not isinstance(other, Clock):
#     #         raise ArithmeticError('Правый операнд должен быть типом Clock')
#     #     return Clock(self.sec * other.sec)
#     #
#     # def __floordiv__(self, other):
#     #     if not isinstance(other, Clock):
#     #         raise ArithmeticError('Правый операнд должен быть типом Clock')
#     #     return Clock(self.sec // other.sec)
#     #
#     # def __mod__(self, other):
#     #     if not isinstance(other, Clock):
#     #         raise ArithmeticError('Правый операнд должен быть типом Clock')
#     #     return Clock(self.sec % other.sec)
#     #
#     # def __sub__(self, other):
#     #     if not isinstance(other, Clock):
#     #         raise ArithmeticError('Правый операнд должен быть типом Clock')
#     #     return Clock(self.sec - other.sec)
#     def __eq__(self, other):
#         # if self.sec == other.sec:
#         #     return True
#         # return False
#         return self.sec == other.sec
#
#     def __gt__(self, other):
#         return self.sec > other.sec
#
#     def __ge__(self, other):
#         return self.sec >= other.sec
#
#
# c1 = Clock(500)
# c2 = Clock(300)
# print(c1.get_format_time())
# print(c2.get_format_time())
# if c1 >= c2:
#     print("Первый больше или равны")
# else:
#     print("Второй больше")
# c1 += c2  # c1 = c1 + c2
# c4 = Clock(300)
# c3 = c1 + c2 + c4
# print(c1.get_format_time())
# print(c2.get_format_time())
# c3 = c1 % c2
# print(c4.get_format_time())
# print(c3.get_format_time())


# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = list(marks)
#
#     def __getitem__(self, item):
#         if 0 <= item < len(self.marks):
#             return self.marks[item]
#         else:
#             raise IndexError("Неверный индекс")
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, int) or key < 0:
#             raise TypeError("Индекс должен быть целым неотрицательным числом")
#
#         if key >= len(self.marks):
#             off = key + 1 - len(self.marks)
#             self.marks.extend([None] * off)
#
#         self.marks[key] = value
#
#     def __delitem__(self, key):
#         if not isinstance(key, int):
#             raise TypeError("Индекс должен быть целым числом")
#         del self.marks[key]
#
#
# s1 = Student("Сергей", [5, 5, 3, 4, 5])
# print(s1[2])
# s1[10] = 4
# del s1[2]
# # print(s1.marks[2])
# print(s1.marks)

# class Clock:
#     DAY = 86400
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#
#         self.sec = sec % self.DAY
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f"{Clock.get_form(h)}:{Clock.get_form(m)}:{Clock.get_form(s)}"
#
#     @staticmethod
#     def get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError("Ключ должен быть строкой")
#
#         if item == "hour":
#             return (self.sec // 3600) % 24
#         elif item == "min":
#             return (self.sec // 60) % 60
#         elif item == "sec":
#             return self.sec % 60
#
#         return "Неверный ключ"
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError("Ключ должен быть строкой")
#
#         if not isinstance(value, int):
#             raise ValueError("Значение должно быть целым числом")
#
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#
#         if key == "hour":
#             self.sec = s + 60 * m + value * 3600
#         elif key == "min":
#             self.sec = s + 60 * value + h * 3600
#         elif key == "sec":
#             self.sec = value + 60 * m + h * 3600
#
#
# c1 = Clock(80000)
# print(c1.get_format_time())
# c1["hour"] = 10
# c1["min"] = 21
# c1["sec"] = 15
# print(c1["hour"], c1["min"], c1["sec"])
# print(c1.get_format_time())

# import random
# from random import choice
# # name = "2"
# # sex = 0
# # if not isinstance(name, str) or not isinstance(sex, str):
# #     raise ValueError("Имя должно быть строкой")
# b = ["M", "F"]
# a = choice(b)
# print(a)


# Полиморфизм

# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_perimetr(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_perimetr(self):
#         return 4 * self.a
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_perimetr(self):
#         return self.a + self.b + self.c
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
# # print(r1.get_per_rect(), r2.get_per_rect())
# s1 = Square(10)
# s2 = Square(20)
# # print(s1.get_per_sq(), s2.get_per_sq())
# t1 = Triangle(1, 2, 3)
# t2 = Triangle(4, 5, 6)
#
# # shape = [r1, r2, s1, s2, t1, t2]
# shape = [Rectangle(3, 4), Triangle(1, 2, 3), Square(10), Square(20), Rectangle(1, 2), Triangle(4, 5, 6)]
#
# for g in shape:
#     print(g.get_perimetr())
#     # if isinstance(g, Rectangle):
#     #     print(g.get_per_rect())
#     # else:
#     #     print(g.get_per_sq())
#
#
# a = '5'
# b = '2'
# c = a + b
# print(c)
# print(a + b)


# class Number:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return self.value + int(a)
#
#
# class Text:
#     def __init__(self, value):  # "Python"
#         self.value = value
#
#     def total(self, a):  # '35'
#         return str(self.value) + str(a)  # "Python35"
#
#
# t1 = Number(10)
# t2 = Text(10)
#
# print(t1.total(35))
# print(t2.total(35))

# class Cat:
#     def __init__(self, type1, name, age):
#         self.type = type1
#         self.name = name
#         self.age = age
#
#     def show_info(self):
#         print(f'Я {self.type}. Меня зовут {self.name}. Мне {self.age} лет.')
#
#     def make_sound(self):
#         print(f'{self.name} мяукает')
#
#
# class Dog:
#     def __init__(self, type1, name, age):
#         self.type = type1
#         self.name = name
#         self.age = age
#
#     def show_info(self):
#         print(f'Я {self.type}. Меня зовут {self.name}. Мне {self.age} лет.')
#
#     def make_sound(self):
#         print(f'{self.name} гавкает')
#
#
# cat = Cat('Кот', 'Рыжик', 2.5)
# dog = Dog('Собака', 'Шарик', 3.5)
#
# animals = [cat, dog]
# for i in animals:
#     i.show_info()
#     i.make_sound()

# class Human:
#     def __init__(self, surname, name, age):
#         self.surname = surname
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print("\n", self.surname, self.name, self.age, end=' ')
#
#
# class Student(Human):
#     def __init__(self, surname, name, age, v1, group, ball):
#         self.v1 = v1
#         self.group = group
#         self.ball = ball
#         super().__init__(surname, name, age)
#
#     def info(self):
#         super().info()
#         print(self.v1, self.group, self.ball, end=" ")
#
#
# class Teacher(Human):
#     def __init__(self, surname, name, age, sub, rating):
#         self.sub = sub
#         self.rating = rating
#         super().__init__(surname, name, age)
#
#     def info(self):
#         super().info()
#         print(self.sub, self.rating, end=" ")
#
#
# class Graduate(Student):
#     def __init__(self, surname, name, age, v1, group, ball, top):
#         self.top = top
#         super().__init__(surname, name, age, v1, group, ball)
#
#     def info(self):
#         super().info()
#         print(self.top, end=" ")
#
#
# group = [
#     Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5),
#     Student("Загидуллин", "Линар", 32, "РПО", "PD_011", 5),
#     Graduate("Шугани", "Сергей", 15, "РПО", "PD_011", 5, "Защита персональных данных"),
#     Teacher("Даньшин", "Андрей", 38, "Астрофизика", 110),
#     Student("Маркин", "Даниил", 17, "ГК", "Python_011", 5),
#     Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)
# ]
#
# for i in group:
#     i.info()


# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f"{self.__class__}: {self.name}"
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# cat = Cat('Пушок')
# print(cat)

# class Point:
#     def __init__(self, *args):
#         print(args)
#         self.__coord = args
#
#     def __len__(self):
#         return len(self.__coord)
#
#
# p = Point(5, 7)
# print(len(p))
#
# import math
#
#
# class Point:
#     __slots__ = ('x', 'y', '__length')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.length = math.sqrt(x * x + y * y)
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, value):
#         self.__length = value
#
#
# pt = Point(1, 2)
# print(pt.length)
# # pt.z = 3
# print(pt.__dict__)


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# pt = Point(1, 2)
# # print(pt.__dict__)
# pt2 = Point2D(1, 2)
# print("pt =", pt.__sizeof__())
# print("pt2 =", pt2.__sizeof__() + pt2.__dict__.__sizeof__())


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point3D(Point):
#     __slots__ = 'z',
#
#     def __init__(self, x, y, z):
#         super().__init__(x, y)
#         self.z = z
#
#
# pt = Point(1, 2)
# pt3 = Point3D(10, 20, 30)
# # # pt3.z = 30
# print(pt3.x, pt3.y, pt3.z)
# print(pt3.__dict__)


# Функторы

# class Counter:
#     def __init__(self):
#         self.__counter = 0
#
#     def __call__(self, *args, **kwargs):
#         self.__counter += 1
#         print(self.__counter)
#
#
# c1 = Counter()
# c1()
# c1()
# c1()
# c2 = Counter()
# c2()
# c2()


# class StripChars:
#     def __init__(self, chars):
#         self.__chars = chars
#
#     def __call__(self, *args, **kwargs):  # Функтор
#         if not isinstance(args[0], str):
#             raise ValueError("Аргумент должен быть строкой")
#         return args[0].strip(self.__chars)
#
#
# s1 = StripChars("?:!.; ")
# print(s1(" !?:Hello World!; "))
#
#
# def strip_chars(chars):
#     def wrap(*args, **kwargs):
#         if not isinstance(args[0], str):
#             raise ValueError("Аргумент должен быть строкой")
#
#         return args[0].strip(chars)
#
#     return wrap
#
#
# s1 = strip_chars("?:!.; ")
# print(s1(" !?:Hello World!; "))


# class Shape:
#     def __init__(self, color):
#         self.color = color
#
#
# class Triangle(Shape):
#     def __init__(self, a, b, c, color):
#         super().__init__(color)
#         self.a = a
#         self.b = b
#         self.c = c
#
#     # def draw(self):  # 11, 6, 6
#     #     lst = [self.a, self.b, self.c]
#     #     n = min(lst)  # 6
#     #     for i in range(n):  # 1
#     #         print('-' * (n - i - 1) + '*' * (2 * i + 1))  # "-" * 4 + "*" * 3
#
#     def draw(self):
#         lst = [self.a, self.b, self.c]
#         n = min(lst)
#         rows = [' ' * (n - i - 1) + '*' * (2 * i + 1) for i in range(n)]
#         return '\n'.join(rows)
#
#
# t = Triangle(11, 6, 6, "yellow")
# # t.draw()
# print(t.draw())


# import random
#
#
# class Cat:
#     def __init__(self, name, age, pol):
#         self.name = name
#         self.pol = pol
#         self.age = age
#
#     def __str__(self):
#         if self.pol == "M":
#             return f"{self.name} is good boy!!!"
#         elif self.pol == "F":
#             return f"{self.name} is good girl!!!"
#         else:
#             return f"{self.name} is good Kitty!!!"
#
#     def __repr__(self):
#         return f"Cat(name='{self.name}', age={self.age}, sex='{self.pol}')"
#
#     def __add__(self, other):
#         # a = [Cat("Ron", 3, "M")]
#         # print("!!!!!!!!!!!!!!!!", a)
#         if self.pol != other.pol:
#             return [Cat(random.choice(['a', 'b', 'c']), 0, random.choice(['M', 'F'])) for _ in range(1, random.randint(2, 7))]
#         else:
#             return "Types are not support!"
#             # raise TypeError("Types are not support!")
#
#
# cat1 = Cat("Tom", 4, "M")
# # print(cat1)
# cat2 = Cat("Elsa", 5, "F")
# # print(cat2)
# # print(cat1 + cat2)
# cat3 = Cat("Ron", 3, "M")
# # print(cat3)
# # print(cat1 + cat3)
# lst = (cat1, cat2, cat2)
# b, c = random.choices(lst, k=2)
# print(b + c)


# Класс как декоратор

# class MyDecorator:
#     def __init__(self, fn):
#         self.func = fn
#
#     def __call__(self, a, b):
#         print('перед вызовом функции')
#         res = self.func(a, b)
#         return str(res) + '\nпосле вызова функции'
#
#
# # def MyDecorator(fn):
# #     def wrap(a, b):
# #         print('перед вызовом функции')
# #         fn(a, b)
# #         print('после вызова функции')
# #
# #     return wrap
#
#
# @MyDecorator
# def func(a, b):
#     return a * b
#
#
# # test = MyDecorator(func)
# # print(test(2, 5))
# print(func(2, 5))


# class Power:
#     def __init__(self, fn):
#         self.fn = fn
#
#     def __call__(self, a, b):
#         return self.fn(a, b) ** 2
#
#
# @Power
# def func(a, b):
#     return a * b
#
#
# print(func(2, 3))


# class MyDecorator:
#     def __init__(self, fn):
#         self.func = fn
#
#     def __call__(self, *args, **kwargs):
#         print('перед вызовом функции')
#         res = self.func(*args, **kwargs)
#         return str(res) + '\nпосле вызова функции\n'
#
#
# @MyDecorator
# def func(a, b):
#     return a * b
#
#
# @MyDecorator
# def func1(a, b, c):
#     return a * b * c


# @MyDecorator
# def func2(a, b, c):
#     return a * b * c
#
#
# print(func(2, 5))
# print(func1(2, 5, 2))
# print(func2(2, 5, c=3))

# class MyDecorator:
#     def __init__(self, arg):
#         self.name = arg
#
#     def __call__(self, fn):
#         def wrap(a, b):
#             print('перед вызовом функции')
#             print(self.name, end=": ")
#             fn(a, b)
#             print('после вызова функции')
#
#         return wrap
#
#
# @MyDecorator("test2")
# def func(a, b):
#     print(a, b)
#
#
# func(2, 5)


# Декорирование методов

# def dec(fn):
#     def wrap(*args, **kwargs):
#         print("*" * 20)
#         fn(*args, **kwargs)
#         print("*" * 20)
#
#     return wrap
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     @dec
#     def info(self):
#         print(f"{self.name} {self.surname}")
#
#
# p1 = Person("Виталий", "Карасев")
# p1.info()


# def dec(fn):
#     def wrap(*args, **kwargs):
#         print("*" * 20)
#         fn(*args, **kwargs)
#         print("*" * 20)
#
#     return wrap

# class Dec:
#     def __init__(self, fn):
#         self.fn = fn
#
#     def __call__(self, *args, **kwargs):
#         print("*" * 20)
#         self.fn(*args, **kwargs)
#         print("*" * 20)
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     @Dec
#     def info(self):
#         print(f"{self.name} {self.surname}")
#
#
# p1 = Person("Виталий", "Карасев")
# Person.info(p1)


# Дескрипторы
# __get__, __set__, __delete__

# class StringD:
#     def __init__(self, value=None):
#         if value:
#             self.set(value)
#
#     def set(self, value):
#         self.__value = value
#
#     def get(self):
#         return self.__value
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = StringD(name)
#         self.surname = StringD(surname)
#
#     # @property
#     # def name(self):
#     #     return self.__name
#     #
#     # @name.setter
#     # def name(self, value):
#     #     self.__name = value
#     #
#     # @property
#     # def surname(self):
#     #     return self.__surname
#     #
#     # @surname.setter
#     # def surname(self, value):
#     #     self.__surname = value
#
#
# p = Person("Ivan", "Petrov")
# p.name.set("Oleg")
# print(p.name.get(), p.surname.get())

# class ValidateString:
#     def __set_name__(self, owner, name):
#         print("Set_name")
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         print("__get__")
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         print("__set__")
#         if not isinstance(value, str):
#             raise ValueError(f"{self.__name} должно быть строкой")
#         instance.__dict__[self.__name] = value
#
#
# class Person:
#     name = ValidateString()
#     surname = ValidateString()
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#
# p = Person("Ivan", "Petrov")
# p.surname = "Oleg"
# print(p.name)
# print(p.surname)

# class Power:
#     def __init__(self, degree):
#         self.degree = degree
#
#     def __call__(self, fn):
#         def wrap(a, b):
#             print('Результат:', fn(a, b) ** self.degree)  #
#
#         return wrap

# def power(degree):
#     def call(fn):
#         def wrap(a, b):
#             print('Результат:', fn(a, b) ** degree)
#
#         return wrap
#
#     return call
#
#
# @power(3)
# def func(a, b):
#     return a * b
#
#
# func(2, 2)

# test = Power(3)
# test1 = test(func)  # __call__
# test1(2, 2)  # wrap

# class NonNegative:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if value < 0:
#             raise ValueError(f'Значение {self.__name} должно быть положительным')
#         instance.__dict__[self.__name] = value
#
#
# class Order:
#     price = NonNegative()
#     qty = NonNegative()
#
#     def __init__(self, name, price, qty):
#         self.name = name
#         self.price = price
#         self.qty = qty
#
#     def total(self):
#         return self.price * self.qty
#
#
# a = Order('apple', 5, 10)
# print(a.total())
# a.price = -20
# a.qty = 10
# print(a.price)
# print(a.total())


# class Integer:
#     @staticmethod
#     def verify_coord(coord):
#         if not isinstance(coord, int):
#             raise TypeError(f'Координата {coord} должно быть целым числом')
#
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         self.verify_coord(value)
#         instance.__dict__[self.name] = value

# class Integer:
#     @staticmethod
#     def verify_coord(coord):
#         if not isinstance(coord, int):
#             raise TypeError(f'Координата {coord} должно быть целым числом')
#
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         # return instance.__dict__[self.name]
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         self.verify_coord(value)
#         # instance.__dict__[self.name] = value
#         setattr(instance, self.name, value)
#
#     def __delete__(self, instance):
#         # del instance.__dict__[self.name]
#         delattr(instance, self.name)
#
#
# class Point3D:
#     x = Integer()
#     y = Integer()
#     z = Integer()
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#
# p1 = Point3D(1, 2, 3)
# del p1.z
# print(p1.__dict__)
# print(p1.y)


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point(5, 10)
# print(p1.__dict__)
# print(getattr(p1, "x"))
# setattr(p1, "x", 6)
# p1.x = 7
# print(p1.__dict__)
# print(p1.x)
# print(hasattr(p1, "z"))


# class MyClass:
#     pass
#
#
# obj = MyClass()
# obj.a = 1
# obj.b = 2
# obj.i = 3
# obj.ireal = 3.5
# obj.integer = 4
# obj.z = 5
#
#
# def incIntsI(obj):
#     for name in obj.__dict__.keys():
#         if name.startswith('i'):
#             val = getattr(obj, name)
#             if isinstance(val, int):
#                 setattr(obj, name, val + 1)
#
#
# print(obj.__dict__)
# incIntsI(obj)
# print(obj.__dict__)

# class Integer:
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         # return instance.__dict__[self.name]
#         return getattr(instance, self.name)
#
#
# class Point3D:
#     x = Integer()
#     y = Integer()
#     z = Integer()
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#
# p1 = Point3D(1, 2, 3)
# print(p1.__dict__)
# print(p1.y)


# Создание модулей

# import geometry.rect
# import geometry.sq
# import geometry.trian
# from geometry import rect, sq, trian
# # import geometry
# # from geometry import *
#
# r1 = rect.Rectangle(1, 2)
# r2 = rect.Rectangle(3, 4)
#
# s1 = sq.Square(10)
# s2 = sq.Square(20)
#
# t1 = trian.Triangle(1, 2, 3)
# t2 = trian.Triangle(4, 5, 6)
#
# shape = [r1, r2, s1, s2, t1, t2]
#
# for g in shape:
#     print(g.get_perimetr())


# from car import electrocar
#
#
# def run():
#     e_car = electrocar.ElectroCar("Tesla", "T", 2020, 50000)
#     e_car.model = "S"
#     e_car.show_car()
#     e_car.description_battery()
#     print(__name__)
#
#
# if __name__ == '__main__':
#     run()


# if __name__ == '__main__':
#     e_car = electrocar.ElectroCar("Tesla", "T", 2020, 50000)
#     e_car.show_car()
#     e_car.description_battery()

# import pickle

# filename = "basket1.txt"
#
# shop_list = {
#     "фрукты": ["яблоки", "манго"],
#     "овощи": ["морковь"],
#     "бюджет": 1000
# }
#
# # with open(filename, "wb") as fh:
# #     pickle.dump(shop_list, fh)
#
#
# with open(filename, 'rb') as fh:
#     shop = pickle.load(fh)
#
# print(shop)


# class Test:
#     num = 35
#     st = "Привет"
#     lst = [1, 2, 3]
#     d = {"first": "a", "second": 2}
#     tpl = (22, 33)
#
#     def __str__(self):
#         return f"Число: {Test.num}\nСтрока: {Test.st}\nСписок: {Test.lst}\nСловарь: {Test.d}\nКортеж: {Test.tpl}"
#
#
# obj = Test()
#
# my_obj = pickle.dumps(obj)
# print(f"Сериализация в строку: \n{my_obj}\n")
#
# l_obj = pickle.loads(my_obj)
# print(f"Десериализация в строку: \n{l_obj}\n")


# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = "test"
#         self.c = lambda x: x * x
#
#     def __str__(self):
#         return f"{self.a} {self.b} {self.c(2)}"
#
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#         del attr['c']
#         return attr
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x * x
#
#
# item1 = Test2()
# item2 = pickle.dumps(item1)
# item3 = pickle.loads(item2)
# print(item3.__dict__)
# print(item3)
# import json
# #
# data = {
#     'name': 'Игорь',
#     'hobbies': ('running', 'sky diving'),
#     True: 20,
#     'children': [
#         {
#             'firstName': 'Alice',
#             'age': 5
#         },
#         {
#             'firstName': 'Bob',
#             'age': 8
#         }
#     ]
# }
# # #
# # # with open("data_file.json", "w") as fw:
# # #     json.dump(data, fw, indent=4)
# # #
# # #
# # # with open("data_file.json", "r") as fw:
# # #     data = json.load(fw)
# # #     print(data)
# #
# json_string = json.dumps(data, ensure_ascii=False)
# # print(type(json_string))
# data = json.loads(json_string)
# print(data)


# Создать класс (любой). Свойства класса сохранить в JSON объект

# class Integer:
#     @staticmethod
#     def verify_coord(coord):
#         if not isinstance(coord, int) or coord < 0:
#             raise TypeError(f"Координата {coord} должна быть целым положительным числом")
#
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         self.verify_coord(value)
#         setattr(instance, self.name, value)
#
#
# class Triangle:
#     a = Integer()
#     b = Integer()
#     c = Integer()
#
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#
# tr1 = Triangle(2, "0", 6)
# print(tr1.__dict__)

# import json
#
#
# class OtherBox:
#
#     def __init__(self, *args, **kwargs):
#         self.base = {
#             'name': 'Павел',
#             'surname': 'Anonim',
#             'age': 18,
#             'id': 1
#         }
#
#     def show_info(self):
#         with open("data_file.json", 'w') as fw:
#             json.dump(self.base, fw)
#         with open("data_file.json", 'r') as fw:
#             data = json.load(fw)
#         print(data)
#
#
# a = OtherBox()
# a.show_info()


# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = "test"
#         # self.c = lambda x: x * x
#
#     def __str__(self):
#         return f"{self.a} {self.b} "
#
#
# data = Test2()
# # d = data.__str__()
# json_string = json.dumps(data.__dict__)  # , default=str
# # print(type(json_string))
# data = json.loads(json_string)
# print(data)

#
# import json
#
#
# class Test2:
#     count = 0
#
#     def __init__(self):
#         self.a = 35
#         self.b = 'test'
#         # self.c = lambda x: x*x
#         self.count += 1
#
#     def __str__(self):
#         return f'{self.a}, {self.b}, {Test2.count}'
#
#
# item1 = Test2()
# item2 = json.dumps(item1.__dict__)
# item3 = json.loads(item2)
# print('Запись в память:', item3)
#
# with open('test2.json', 'w') as fw:
#     json.dump(Test2().__str__(), fw)
#
# with open('test2.json', 'r') as fw:
#     data = json.load(fw)
#     print('Запись в файл:', data)


# import json
# from random import choice
#
#
# def get_person():
#     name = ''
#     tel = ''
#
#     letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(letter)
#
#     while len(tel) != 10:
#         tel += choice(nums)
#
#     person = {
#         'name': name,
#         'tel': tel
#     }
#     return person, tel
#
#
# def write_json(person_dict, num):  # {}
#     try:
#         data = json.load(open('persons.json'))  # [{}, {}, {}, {}, {}]
#     except FileNotFoundError:
#         data = {}
#
#     data[num] = person_dict  # [{}, {}, {}, {}, {}, {}]
#     with open('persons.json', 'w') as f:
#         json.dump(data, f, indent=2)  # [{}, {}, {}, {}, {}, {}]
#
#
# for i in range(5):
#     write_json(get_person()[0], get_person()[1])  # {"name": "dadcfec", "tel": "3910610858"}


# import json
#
#
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __str__(self):
#         # a = ""
#         # for i in self.marks:
#         #     # a += f"{i}, "
#         #     a += str(i) + ", "
#         a = ", ".join(map(str, self.marks))  # self.marks = ['5', '4', '3', '4', '5', '3']
#         return f"Студент: {self.name}: {a}"  # [:-2]
#
#     def add_marks(self, mark):
#         self.marks.append(mark)
#
#     def delete_mark(self, index):
#         self.marks.pop(index)
#
#     def edit_mark(self, index, new_mark):
#         self.marks[index] = new_mark
#
#     def average_mark(self):
#         return round(sum(self.marks) / len(self.marks), 2)
#
#     @staticmethod
#     def dump_to_json(stud, filename):
#         try:
#             data = json.load(open(filename))
#         except FileNotFoundError:
#             data = []
#
#         data.append({"name": stud.name, "marks": stud.marks})
#         with open(filename, 'w') as f:
#             json.dump(data, f, indent=2)
#
#     @staticmethod
#     def load_to_file(filename):
#         with open(filename, 'r') as f:
#             print(json.load(f))
#
#
# class Group:
#     def __init__(self, students, group):
#         self.students = students
#         self.group = group
#
#     def __str__(self):
#         # a = ''
#         # for i in self.students:
#         #     a += str(i) + "\n"
#         a = '\n'.join(map(str, self.students))
#         return f"Группа: {self.group}\n{a}"
#
#     def add_student(self, student):
#         self.students.append(student)
#
#     def remove_student(self, index):
#         return self.students.pop(index)
#
#     @staticmethod
#     def change_group(group1, group2, index):
#         return group2.add_student(group1.remove_student(index))
#
#     @staticmethod
#     def dump_group(file, group):
#         try:
#             data = json.load(open(file))
#         except FileNotFoundError:
#             data = []
#
#         with open(file, 'w') as f:
#             stud_list = []
#             for i in group.students:
#                 stud_list.append([i.name, i.marks])
#             data.append(stud_list)
#             json.dump(data, f, indent=2)
#
#     @staticmethod
#     def upload_journal(file):
#         with open(file, 'r') as f:
#             print(json.load(f))
#
#
#
# st1 = Student('Bodnya', [5, 4, 3, 4, 5, 3])
# # print(st1)
# # st1.add_marks(4)
# # print(st1)
# # st1.delete_mark(3)
# # print(st1)
# # st1.edit_mark(2, 4)
# # Student.dump_to_json(st1, 'student.json')
# # Student.load_to_file('student.json')
# # print(st1)
# # print(st1.average_mark())
# st2 = Student('Nikolaenko', [2, 3, 5, 4, 2])
# # Student.dump_to_json(st2, 'student.json')
# # Student.load_to_file('student.json')
# st3 = Student('Birukov', [3, 5, 3, 2, 5, 4])
# sts = [st1, st2]
# my_group = Group(sts, "ГК Python")
# # # print(my_group)
# # # print()
# # my_group.add_student(st3)
# # # print(my_group)
# # # print()
# # my_group.remove_student(1)
# # print(my_group)
# group22 = [st3]
# # print()
# my_group2 = Group(group22, "ГК Web")
# # Group.dump_group('group.json', my_group)
# # Group.dump_group('group.json', my_group2)
# Group.upload_journal('group.json')
# # print(my_group2)
# # print()
# # Group.change_group(my_group, my_group2, 0)
# # print(my_group)
# # print()
# print(my_group2)

# import requests
# import json
#
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# todos = json.loads(response.text)
#
# # print(todos[:10])
# # print(type(todos))
#
# todos_by_user = {}  # {1: 11, 2: 1}
#
# for todo in todos:
#     if todo["completed"]:
#         try:
#             todos_by_user[todo["userId"]] += 1  # todos_by_user[2] += 1
#         except KeyError:
#             todos_by_user[todo["userId"]] = 1  # todos_by_user[1] = 1
# print(todos_by_user)
#
#
# def ind(x):
#     return x[1]
#
#
# top_users = sorted(todos_by_user.items(), key=ind, reverse=True)  # key=lambda x: x[1]
# print(top_users)
#
# max_complete = top_users[0][1]
# print(max_complete)
#
# users = []
# for user, num_complete in top_users:
#     if num_complete < max_complete:
#         break
#     users.append(str(user))
#
# # print(users)
# max_users = " and ".join(users)
#
# s = "s" if len(users) > 1 else ""
# print(f"user{s} {max_users} completed {max_complete} TODOs")
#
#
# def keep(tod):
#     is_complete = tod['completed']
#     has_max_count = str(tod['userId']) in users
#     return is_complete and has_max_count
#
#
# with open('filtered_data_file.json', 'w') as f:
#     filtered_todos = list(filter(keep, todos))
#     json.dump(filtered_todos, f, indent=2)
#
# with open('filtered_data_file.json', 'r') as f:
#     data = json.load(f)
#     print(data)


# csv (Comma Separated Values) - переменные, разделенные запятыми.

import csv

# with open("data.csv", 'r') as r_file:
#     file_reader = csv.reader(r_file, delimiter=";")
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         else:
#             print(f"    {row[0]} - {row[1]}. Родился в {row[2]} году.")
#         count += 1
#     print(f"Всего в файле {count} строки.")

# with open("data.csv", 'r') as r_file:
#     field_names = ['Имя', 'Профессия', 'Год рождения']
#     file_reader = csv.DictReader(r_file, delimiter=";", fieldnames=field_names)
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         print(f"    {row['Имя']} - {row['Профессия']}. Родился в {row['Год рождения']} году.")
#         count += 1
#     print(f"Всего в файле {count} строки.")


# with open('student.csv', mode="w") as f:
#     writer = csv.writer(f, delimiter=";", lineterminator="\r")
#     writer.writerow(["Имя", "Класс", "Возраст"])
#     writer.writerow(["Женя", "9", "15"])
#     writer.writerow(["Саша", "5", "12"])
#     writer.writerow(["Маша", "11", "18"])


# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
#
#
# with open('data_sw.csv', mode="w") as f:
#     writer = csv.writer(f, delimiter=";", lineterminator="\r")
#     # for row in data:
#     #     writer.writerow(row)
#     writer.writerows(data)
#
# with open('data_sw.csv') as f:
#     print(f.read())


# with open('stud.csv', mode="w") as f:
#     names = ["Имя", "Возраст"]
#     file_writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=names)
#     file_writer.writeheader()
#     file_writer.writerow({"Имя": "Саша", "Возраст": "6"})
#     file_writer.writerow({"Имя": "Маша", "Возраст": "15"})
#     file_writer.writerow({"Имя": "Вова", "Возраст": "14"})


# data = [{
#     'hostname': 'sw1',
#     'location': 'London',
#     'model': '3750',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw2',
#     'location': 'Liverpool',
#     'model': '3850',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw3',
#     'location': 'Liverpool',
#     'model': '3650',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw4',
#     'location': 'London',
#     'model': '3650',
#     'vendor': 'Cisco'
# }]
#
# with open('dictwriter.csv', 'w') as f:
#     writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=list(data[0].keys()))
#     writer.writeheader()
#     for d in data:
#         writer.writerow(d)


# Парсинг

# from bs4 import BeautifulSoup
# import re


# def get_copywriter(tag):
#     whois = tag.find("div", class_="whois").text.strip()
#     if "Copywriter" in whois:
#         return tag
#     return None

# def get_salary(s):
#     pattern = r"\d+"
#     # res = re.findall(pattern, s)[0]
#     res = re.search(pattern, s).group()
#     print(res)
#
#
# f = open('index.html', encoding="utf-8").read()
# soup = BeautifulSoup(f, "html.parser")
#
# salary = soup.find_all("div", {"data-set": "salary"})
# for i in salary:
#     get_salary(i.text)

# copywriter = []
# row = soup.find_all('div', class_="row")
# for i in row:
#     cw = get_copywriter(i)
#     if cw:
#         copywriter.append(cw)
#
# print(copywriter)


# row = soup.find('div', class_="name").text
# row = soup.find_all('div', class_="name")
# print(row)
# for r in row:
#     print(r.text)
# row = soup.find_all("div", class_="row")[1].find("div", class_="links")
# print(row)
# row = soup.find_all("div", {"data-set": "salary"})
# print(row)
# row = soup.find("div", string="Alena").parent.parent
# row = soup.find("div", string="Alena").find_parent(class_="row")
# print(row)
# row = soup.find("div", id="whois3").find_next_sibling()
# row = soup.find("div", id="whois3").find_previous_sibling()
# print(row)


# import requests


# r = requests.get("https://ru.wordpress.org/")
# print(r.headers)
# print(r.headers['content-type'])
# print(r.content)
# print(r.text)

# import requests
# from bs4 import BeautifulSoup
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find("header", id="masthead").find("p", class_="site-title").text
#     return p1
#
#
# def main():
#     url = "https://ru.wordpress.org/"
#     print(get_data(get_html(url)))
#
#
# if __name__ == '__main__':
#     main()

# import requests
# from bs4 import BeautifulSoup
# import re
# import csv
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def refined(s):
#     res = re.sub(r"\D+", "", s)
#     return res
#
#
# def write_csv(data):
#     with open("plugins.csv", "a") as f:
#         writer = csv.writer(f, lineterminator="\r", delimiter=";")
#         writer.writerow((data['name'], data['url'], data['rating']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find_all("section", class_="plugin-section")[3]
#     plugins = p1.find_all('article')
#
#     for plugin in plugins:
#         name = plugin.find("h3").text
#         url = plugin.find("h3").find("a").get("href")  # ["href"]
#         rating = plugin.find("span", class_="rating-count").find("a").text
#         r = refined(rating)
#         data = {'name': name, "url": url, "rating": r}
#         write_csv(data)
#     # return len(plugins)
#
#
# def main():
#     url = "https://ru.wordpress.org/plugins/"
#     get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()


# import requests
# from bs4 import BeautifulSoup
# import csv
# import re
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def refine_cy(s):
#     return s.split()[-1]
#
#
# def refine_snippet(s):
#     res = [ord(c) for c in s if ord(c) < 9000]
#     res1 = ''.join([chr(c) for c in res])
#     return res1
#
#
# def write_csv(data):
#     with open("plugins1.csv", "a", encoding="utf-8-sig") as f:
#         writer = csv.writer(f, lineterminator="\r", delimiter=";")
#         writer.writerow((data['name'],
#                          data['url'],
#                          data['snippet'],
#                          data['cy']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     elements = soup.find_all("article", class_="plugin-card")
#     for el in elements:
#         try:
#             name = el.find("h3").text
#         except ValueError:
#             name = ""
#
#         try:
#             url = el.find("h3").find("a").get("href")
#         except ValueError:
#             url = ""
#
#         try:
#             snippet = el.find("div", class_="entry-excerpt").text.strip()
#             snippet1 = refine_snippet(snippet)
#         except ValueError:
#             snippet1 = ""
#         # print(snippet1)
#
#         try:
#             c = el.find("span", class_="tested-with").text.strip()
#             cy = refine_cy(c)
#         except ValueError:
#             cy = ""
#
#         data = {
#             'name': name,
#             'url': url,
#             'snippet': snippet1,
#             'cy': cy
#         }
#
#         write_csv(data)
#
#
# def main():
#     for i in range(26):
#         url = f"https://ru.wordpress.org/plugins/browse/blocks/page/{i}/"
#         get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()


# from parsers import Parsers
#
#
# def main():
#     pars = Parsers("https://www.ixbt.com/live/index/news/", "new.txt")
#     pars.run()
#
#
# if __name__ == '__main__':
#     main()

import sqlite3 as sq

# con = sq.connect('profile.db')
# cur = con.cursor()
#
# cur.execute("""
# """)
#
# con.close()

# with sq.connect('profile.db') as con:
#     cur = con.cursor()
#     # cur.execute("""CREATE TABLE IF NOT EXISTS users(
#     # id INTEGER PRIMARY KEY AUTOINCREMENT,
#     # name TEXT NOT NULL,
#     # summa REAL,
#     # data BLOB
#     # )""")
#     cur.execute("DROP TABLE users")


# with sq.connect('users.db') as con:
#     cur = con.cursor()
#     cur.execute("""
#     DROP TABLE person_table
#     """)

    # cur.execute("""
    # CREATE TABLE IF NOT EXISTS person(
    # id INTEGER PRIMARY KEY AUTOINCREMENT,
    # name TEXT NOT NULL,
    # phone BLOB NOT NULL DEFAULT '+79090000000',
    # age INTEGER NOT NULL CHECK(age>15 AND age<70),
    # email TEXT UNIQUE
    # )""")

with sq.connect('db_3.db') as con:
    cur = con.cursor()
    cur.execute("""
    SELECT *
    FROM T1
    ORDER BY FName
    LIMIT 2, 5
    """)

    res2 = cur.fetchmany(4)
    res = cur.fetchone()
    res1 = cur.fetchall()
    print(res2)
    print(res)
    print(res1)
    # for res in cur:
    #     print(res)

