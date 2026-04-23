# python -m venv .env
# .\.env\Scripts\activate
# from fontTools.varLib.instancer.names import pruningUnusedNames
# from gc import collect
# from turtledemo.penrose import start

# name_new = "Иван"
# name = "Антон"
# age = 20
# print('Hello ' + name_new + ". I am " + str(age))
#
# print(type(name))
# print(type(age))
# print(id(name))
# print(id(age))
#
# a = b = c = 1
# print(a, b, c)
#
# a, b, c = 5, "Hello", 9.2
# print(a, b, c)
# import keyword
# print(keyword.kwlist)
#
# a = 5
# print(a)
# a = 6
# print(a)
#
# PI = 3.14
# print(PI)
# PI = 2
# print(PI)
#
# a = 1
# b = 2
# print("a:", a)
# print("b:", b)
# # c = a  # c = 1
# # a = b  # a = 2
# # b = c  # b = 1
# a, b = b, a
# print("a:", a)
# print("b:", b)
#
# print("строка \nТекстовые последовательности или строки (string) – это набор символов, заключенный в кавычки.\nТекстовые последовательности или строки (string) – это набор символов, заключенный в кавычки. символов")
# print('строка \
#       символов')
#
# print("Документ \"script.py\" находтся \rпо заданному пути: \n\tD:\\Python\\project")
#
# print(type(46460))
# print(type(4.44564156))
# print(445641564454156341563416548674874896749)
# print(4.445641564454156341563416548674874896749)
#
# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(5 / 2)
# print(5 // 2)
# print(5 ** 2)
# print(5 % 2)
#
# a = 5
# b = 7
# c = 3
# s = a + b + c
# print("Сумма:", s)
# print("Произведение:", a * b * c)
# print("Среднее арифметическое:", s / 3)
#
# number = 6 + 4 * 5 ** 2 + 7
# print(number)
# number = (6 + 4) * (5 ** 2 + 7)
# print(number)
#
# num = 4321  # 432
# print("Исходное число:", num)
# a = num % 10
# print(a)
# num = num // 10
# # print(num)
# b = num % 10
# print(b)
# num = num // 10
# # print(num)
# c = num % 10
# print(c)
# num = num // 10
# # print(num)
# d = num % 10
# print(d)
# print(a * 1000 + b * 100 + c * 10 + d)
#
# num = 9573  # 432
# print("Исходное число:", num)
# res = (num % 10) * 1000
# num = num // 10  # 432
# res += (num % 10) * 100
# num = num // 10
# res += (num % 10) * 10
# num = num // 10
# res += num % 10
# print(res)
#
# a = int(input("Введите число: "))
# # a = int(a)
# print(type(a))
# print(a * 2)
#
# a = 10
# b = 2
# print("a:", a)
# print("b:", b)
# a = a + b  # a = 10 + 2 = 12
# b = a - b  # b = 12 - 2 = 10
# a = a - b  # a = 12 - 10 = 2
# print("a:", a)
# print("b:", b)
#
# # Функции преобразования типов
# # int() - числовой тип
# # str() - строковый тип
# # float() - вещественный тип
# # bool() - булевый тип
#
# num1 = "2"
# num2 = 3
# res = int(num1) + num2
# # res = num1 + str(num2)
# print(res)
# print(type(res))
#
# print(int(3.8))
# print(round(3.8954144165341, 5))
#
# print(5 / 2)
#
# a = '5.2'
# # b = 10
# # c = float(a) + b
# # print(c)
# # print(type(c))
#
# name = "Виктор"
# age = 28
# print("Меня зовут", name, ". Мне", age, "лет.")
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print("Меня зовут ", name, ". Мне ", age, " лет.", sep="---", end=" ")
# print("Я учу Python")
#
# num = int(input("Введите число: "))
# power = int(input("Введите степень: "))
# res = num ** power
# print("Число", num, "в степень", power, "равно:", res)
#
# b1 = True
# # b2 = False
# # print(b1 + 5)
# # print(b2 + 5)
# print(type(b1))
#
# print(bool("python"))
# print(bool(""))  # False
# print(bool(" "))
# print(bool(-15.2))
# print(bool(0))  # False
# print(bool(False))  # False
# print(bool(None))  # False
#
# test = None
# print(test)
# print(type(test))
# test = 5
# print(test)
# print(type(test))
#
# print(7 == 7)
# print(7 + 2 == 7)
# print(7 + 2 != 7)
# print(8 > 5)
# print(8 < 5)
# print(8 >= 8)
# print(8 <= 5)
# print('привет' > 'Привет')
#
#
# print(2 < 14 < 9)
# print(2 * 5 > 7 > 4 + 3)
#
# a = 10
# b = 5
# c = a == b
# print(a, b, c)
#
# print(5 - 3 == 2 and 1 + 3 == 4)  # True (True : True)
# print(5 - 3 == 2 and 1 + 3 < 4)  # False (True : False)
# print(5 - 3 > 2 and 1 + 3 == 4)  # False (False : True)
# print(5 - 3 > 2 and 1 + 3 < 4)  # False (False : False)
#
#
# print(5 - 3 == 2 or 1 + 3 == 4)  # True (True : True)
# print(5 - 3 == 2 or 1 + 3 < 4)  # True (True : False)
# print(5 - 3 > 2 or 1 + 3 == 4)  # True (False : True)
# print(5 - 3 > 2 or 1 + 3 < 4)  # False (False : False)
#
#
# print(not 9 - 5)
# print(not 5 - 5)
#
# cnt = 15
# if cnt < 10:
#     cnt += 1
# print(cnt)
#
# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ запрещен")
#
# a = 15
# b = 5
# # if a > b:
# #     print("a > b")
# # elif a < b:
# #     print("b > a")
# # else:
# #     print("b == a")
#
# if a > b:
#     print("a > b")
# if a < b:
#     print("b > a")
# if a == b:
#     print("b == a")
#
# a = input("Введите первую сторону: ")
# b = input("Введите вторую сторону: ")
# c = input("Введите третью сторону: ")
#
# # if a == b and b == c and c == a:
# if a == b == c:
#     print('Треугольник равносторонний')
# elif a == b or c == a or b == c:
#     print('Треугольник равнобедренный')
# # elif not (a == b and b == c and c == a):
# # elif a != b and b != c and c != a:
# else:
#     print("Треугольник разносторнний")
#
# num1 = 10
# num2 = 20
# num3 = 20
# if num1 == num2 == num3:
#     print("Равносторонний")
# elif num1 == num2 or num1 == num3 or num2 == num3:
#     print("Равнобедренный")
# else:
#     print("Разносторонний")
#
# day = int(input("Введите день недели (цифрой): "))
# if 1 <= day <= 5:  # (day >= 1) and (day <= 5):
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
#
# m = int(input("Введите номер месяца: "))
# month = int(input('Введите номер месяца: '))
# if month == 1 or month == 2 or month == 12:
#     print('Зима')
# elif month == 3 or month == 4 or month == 5:
#     print('Весна')
# elif month == 6 or month == 7 or month == 8:
#     print('Лето')
# elif month == 9 or month == 10 or month == 11:
#     print('Осень')
# else:
#     print('Ошибка')
#
# month = int(input('Введите номер месяца: '))
# if 1 <= month <= 12:
#     if 3 <= month <= 5:
#         print('Весна')
#     elif 6 <= month <= 8:
#         print('Лето')
#     elif 9 <= month <= 11:
#         print('Осень')
#     else:
#         print('Зима')
# else:
#     print("Ошибка ввода данных")
#
#
# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     if n == 1:
#         print("На ветке", n, "ворона")
#     if 2 <= n <= 4:
#         print("На ветке", n, "вороны")
#     # else:
#     if 5 <= n <= 9 or n == 0:
#         print("На ветке", n, "ворон")
# else:
#     print("Ошибка ввода данных")
#
# # (условие ? True : False)
#
# a, b = 10, 20
#
# minim = "a == b" if a == b else "a > b" if a > b else "b > a"
# print(minim)
#
#
# a = 5
# b = 0
# print(a / b)
#
# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Неправильные данные")
# else:
#     print("Все нормально. Вы ввели числа", n, "и", m)
# finally:
#     print("Конец программы")
# # except ValueError:
# #     print("Нельзя вводить строки")
# # except ZeroDivisionError:
# #     print("Нельзя делить на ноль")
#
# print("OK!!!")
#
# try:
#     a = int(input('Введите первое значение: '))
#     b = int(input('Введите второе значение: '))
#     print(a + b)
# except ValueError:
#     print(str(a) + str(b))
#
#
# a = input('Введите первое число: ')
# b = input('Введите второе: ')
# try:
#     a = int(a)  # a = 2
#     b = int(b)  # b = пять
# except ValueError:
#     a = str(a)
#     b = b
# finally:
#     print(a + b)
#
#
# # while условие:
# #     блок инструкций
#
# i = 10
# while i >= 0:
#     print("i =", i)
#     i -= 1  # i = i + 1
#
# i = 1
# while i <= 20:
#     if i % 2:
#         print(i, end=" ")
#     i += 1
#
# i = 1000
# while i >= 1:
#     print(i, end=" ")
#     i //= 10
#
# n = int(input("Укажите количество символов: "))
# i = 0
# while i < n:
#     print("*", end="")
#     i += 1
#
# n = int(input("Укажите количество символов: "))
# while n > 0:
#     print("*", end="")
#     n -= 1
#
#
# n = int(input('Введите число: '))  # 1
# m = int(input('Введите число: '))  # 5
# # i = n
# res = 0
# while n <= m:
#     if n % 2:
#         res += n  # res = res + n
#         print(n, end=" ")
#     n += 1
# print("Сумма целых нечетных чисел:", res)
#
#
# n = input("Введите целое число: ")
#
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое")
#         n = input("Введите целое число: ")
#
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")
#
# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен!")
#
# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1
#
# while True:
#     n = int(input("Введите положительное целое число: "))
#     if not n < 0:
#         break
#
# print(n)
# res = 1
# while True:
#     n = int(input('Введите число: '))
#     if n == 0:
#         break
#     res *= n
# print("Результат:", res)
#
#
# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i =", i)

# n = int(input("Количество символов: "))
# sim = input("Тип символа: ")
# orient = input("0 - горизонтально\n1 - Вертикально: ")
# i = 0
# while i < n:
#     if orient == "0":
#         print(sim, end='')
#     elif orient == "1":
#         print(sim)
#     else:
#         print("Символ не предусмотренн")
#         break
#     i += 1

# kol = int(input("Количество чисел последовательности:"))
# n = float(input("Введите число: "))
# summa = n
# minim = n
# maxim = n
# i = 1
# while i < kol:
#     n = float(input("Введите число: "))
#     summa += n
#     if minim > n:
#         minim = n
#     if maxim < n:
#         maxim = n
#     i +=1
#
# print("Среднее арифметическое",summa / kol)
# print("Минимальное", minim)
# print("Максимальное", maxim)

# i = 1
# while i < 5:
#     print("Внешний цикл. i = ",i)
#     j = 1
#     while j < 5:
#         print("Вложенный цикл. j =", j)
#         j += 1
#     i += 1

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1

# symb = input("ВВедите символ: ")
# i = 0
# while i < 3:
#     j = 0
#     while j < 6:
#         print("^", end="")
#         j += 1
#     print()
#     i += 1


# i = 0
# while i < 7:
#     j = 0
#     while j < 20:
#         if i % 2 ==0:
#             print("*", end="")
#         else:
#             print("^", end="")
#         j += 1
#     print()
#     i += 1

# for(let i = 0;i < 5; i++){
#     console.log(i)
# }

# for element in collection:
#     print(element)

# for i in "Hello":
#     print(i)

# for i in 5, 6, 7, 8, 9:
#     print(i)

# range(start, stop, step)
# print(range(2,5))

# for i in range(2, 100, 4):
#     print(i, end=' ')

# for i in range(-200, -100, 4):
#     print(i, end=' ')

# a = int(input("Введите целое число: "))
# for i in range(1, a + 1, 1):
#     if a % i ==0:
#         print(i, end=" ")

# for i in range(10, 1000):
#     if i % 100 == i // 100:
#         print(i, end=" ")

# for i in range(5):
#     print(i, end=' ')
#     if i == 1:
#         break
# else:
#     print("Конец цикла")

# for i in range(3):
#     print("+++")
#     for j in range(2):
#         print('---')

# w = int(input("Ширина: "))
# h = int(input("Высота: "))
#
# for i in range(h):
#     for j in range(w):
#         print("*",end="")
#     print()

# w = int(input("Ширина: "))
# h = int(input("Высота: "))
# w = 16
# h = 4
#
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print("*", end='')
#         else:
#             print(' ', end='')
#     print()

# n = [i for i in range(6)]
# print(n)

# n = [i for i in range(6) if i % 2 == 0]
# print(n)

# n = [i * 2 for i in "Hello"]
# print(n)

# n = [i for i in "Hello"]
# print(n)

# n = [5, 6, [7, 8, 9], "Hello", 1, 2, True]
# print(n)
# print(type(n))
# print(n[0])
# print(n[2][0])
# print(n[3])
# print(n[3][1])
# print(n[-2])

# n[1] = 256
# n[3] += "100"
# n[-7] = 45
# print(n)
# print(len(n))

# s = [1, 2, 3]
# print([5] * 5)
# print(s * 5)
# b = list('HELLO')
# print(b)

# n = list(range(2, 10, 2))
# n = [2, 4, 6, 8]
# n2 = [2, 4, 6, 8]
# n = "HELLO"
# n2 = "hello"

# print(n)
# print(id(n))
# print(n2)
# print(id(n2))
#
# if n == n2:
#     print("Списки равны")
# else:
#     print("Списки разные")
#
# if n is n2:
#     print("Списки подобны")
# else:
#     print("Списки не подобны")

# [выражение for переменная in последовательность]

# n = 5
#
# a = [i for i in range(1, n + 1)]
# print(a)

# n = 5
#
# for i in range(1, n + 1):
#     print(i ** 2, end=" ")

# a = [1, 2, 3]
# b = [4, 5]
# c = a + b
# print(c)
# d = b * 3
# print(d)

# a = [0] * int(input("Введите количество элементов списка: "))
# print(a)
# for i  in range(len(a)):
#     a[i] = int(input("--> "))
# print(a)

# a = [int(input("-> ")) for  i in range(int(input("n = ")))]
# print(a)

# print([int(input("-> ")) for  i in range(int(input("n = ")))])

# n = [2, 4, 6, 8, 2, 4, 6, 8]
#
# for i in range(len(n)):
#     print(n[i], end=" ")
#
# print()
# for elem in n:
#     print(elem, end=" ")


# a = [int(input("-> ")) for  i in range(int(input("n = ")))]
# n = [-3, 9, -5, -1]
#
# b = 0
# for i in n:
#     if i < 0:
#         b += i
# print(b)
#
# b = 0
# for i in range(len(n)):
#     if n[i] < 0:
#         b += n[i]
# print(b)

# n = list(range(21, 41))
# print(n)
# s = k = 0
# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         k += 1
#     else:
#         s += n[i]

# for i in n:
#     if i % 2 == 0:
#         k += 1
#     else:
#         s += i
#
# print("Количество четных элементов списка: ", k)
# print("Сумма нечетных элементов: ", s)

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# s = k = 0
# for i in range(len(a)):
#     if a[i] != 0:
#         s += a[i]
#         k += 1
# print(s / k)

# a = [7, 9, 2, 1, 17, 45]
# a[0], a[-1] = a[-1], a[0]
# print(a)

# срез списка[start: stop: step]

# s = [5, 6, 7, 8, 9, 33]
# # print(s[1:4])
# # print(s[2:])
# # print(s[:2])
# # print(s[-1:0:-1])
# # print(s[1:50])
# print(s[6:7])

# a = [1, 2, 3, 4, 5, 6, 7]
# print(a[:])
# print(a[::-1])
# print(a[::2])
# print(a[1::2])
# print(a[-1:])
# print(a[3:4])
# print(a[4:])
# # print(a[-3:1:-1])
# print(a[-3:-6:-1])
# print(a[2:5])

# s = [5, 9, 3, 7, 1, 8]
# s[1:3] = [0, 0, 0, 0]
# print(s)
# # s[1:3] = "HELLO"
# # print(s)
# # s[2] = 20
# print(len(s))
# s[100:] = [9, 9, 8, 6, 5, 3, 21, 1, 3]
# print(s)
# print(len(s))

# Методы списков


# s = [5, 9, 3, 7, 1, 8]
#
# s.append(99)  # Добавляет один элемент в конец списка
# print(s)
# s.extend([1, 2, 3]) #добавляет список в конец основного списка
# print(s)
# s.extend("HELLO")
# print(s)
# s.insert(1, 100) #добавляет элемент по индексу(первый параметр), с заданным значеным(второй параметр)
# print(s)

# s = []
# n = int(input("n = "))
# for num in range(n):
#     x = int(input("--> "))
#     s.append(x)
# print(s)


# s = []
# n = int(input("n = "))
# for num in range(n):
#     x = int(input("--> "))
#     if x % 3 ==0:
#         s.append(x)
#     else:
#         print(x, "не делится на 3")
# print(s)

# a = [5, 3, 3, 7, 8, 3, 9, 0, 3, 3, 7, 8, 3, 9, 0]
# b = [6, 46, 8, 56, 3, 3, 9, 3, 3, 3]
# c = []
# print('a = ', a)
# print('b = ', b)
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)

# a = [1, 2, 3]
# b = [11, 22, 33, 7, 8, 9]
# c = []
# print('a = ', a)
# print('b = ', b)

# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# print(c)

# i = 0
# while i < len(a):
#     c.append(a[i])
#     c.append(b[i])
#     i += 1
# print(c)
#
#
# a = [1, 2, 3]
# b = [11, 22, 33]
# c = []
# print('a = ', a)
# print('b = ', b)
#
# if len(b) > len(a):
#     for i in range(len(a)): # 0-3
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)): # 3- конца
#         c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
# print(c)

# s = [5, 9, 3, 7, 1, 0]
# s[3:] =[]
# print(s)
# s.remove(9) # удаляет элемент по значению
# print(s)
# last =  s.pop(1) # удаляет и возвращает элемент по индексу, без параметра удаляет последний
# print(s)
# print(last)
# s.clear() #очищает список удаляя все элементы
# print(s)
# del s[2::2]
# print(s)

# s = [int(input("-> ")) for i in range(int(input("n = ")))]
# k = int(input("k = "))
# # s.pop(k)
#
# del s[k]
# print(s)

# s = [5, 9, 3, 7, 1, 0, 2, 8, 3, 8, 3]
# num = s.count(1) # количество заданных значений в списке
# print(num)
# print(s)
# # ind = s.index(3)
# ind = s.index(3, 9 )
#
# print(ind)

# a = [1, 2, 3]
# b = a
# print('a = ', a)
# print('b = ', b)
# a.append(20)
# print('a = ', a)
# print('b = ', b)
# a[0] = 9
# b[3] = 55
# print('a = ', a)
# print('b = ', b)
# print('a = ', id(a))
# print('b = ', id(b))

# a = [1, 2, 3]
# b = a.copy()
# print('a = ', a)
# print('b = ', b)
# a.append(20)
# print('a = ', a)
# print('b = ', b)
# a[0] = 9
# b[2] = 55
# print('a = ', a)
# print('b = ', b)
# print('a = ', id(a))
# print('b = ', id(b))

# s = [5, 7, 9, 3, 5, 3, 4, 7, 6, 9, 2, 2, 7, 7, 7, 0, 0, 4, 4, 6, 7]
# print(s)
# # s.reverse() #Переворачивает список
# # s.sort(reverse=True) # Сортирует список в порядке возрастания, изменяя список, reverse=True - сортировака в порядке убывания
# # print(s)
#
# a = sorted(s, reverse=True) # Сортирует список в порядке возрастания, Не изменяя список
# print(a)
# print(s)

# s2 = ["Дима", "Настя", "Маша", "Яна", "Амин", "Вася"]
# # s2.sort(key=len, reverse=True)
# s2.sort()
# print(s2)

# import random
#
# # print(random.random())
# # print(random.randint(10, 15))
# print(random.randrange(0, 10, 2))

# from random import randint, randrange
# print(randint(10, 15))
# print(randrange(0, 10, 2))


import random as r

# print(r.randint(10, 15))
# print(r.randrange(0, 10, 2))
# s2 = ["Дима", "Настя", "Маша", "Яна", "Амин", "Вася"]
# print(r.choice(s2))

# s = [5, 7, 9, 3, 5, 3, 4, 7, 6, 9, 2, 2, 7, 7, 7, 0, 0, 4, 4, 6, 7]
# print(r.choice(s))
# print(r.choices(s, k=5))
# r.shuffle(s)
# print(s)

# print(r.uniform(10.5, 25.9))
# print(round(r.uniform(10.5, 25.9), 2))

# mas = [r.randint(0, 100) for i in range(10)]
# print(mas)

# lst = [5, 4, 8, 9, 5, 3]
# # print(len(lst))
# # print(max(lst))
# # print(min(lst))
# print(sum(lst))
#
# sum_list = [1, 2, 3]
# print(min(sum_list))
# print(sum(lst))

# x = [r.randint(0, 100) for i in range(0, 10)]
# print(x)
# m = max(x)
# print("Max", m)
# x.remove(m)
# x.insert(0, m)
# print(x)


# x = [r.randint(-100, 100) for i in range(0, 10)]
# print(x)
# x.sort(reverse=True)
# print(x)

# x = [r.randint(0, 100) for i in range(0, 10)]
# print(x)
# m = min(x)
# print("Min", m)
# b = x.index(m)
# print("index", b)
# del x[:b]
# print(x)

# x = list('1a2b3c4d5e6f')
# print(x)
# print('a' in x)
# print('x' in x)
# print('a' not in x)
# print('x' not in x)

# lst = []
# # if len(lst) == 0:
# #     print("Список пустой")
# if not lst:
#     print("Список пустой")

# n1 = int(input("Размер cписка 1: "))
# n2 = int(input("Размер cписка 2: "))
# a = [r.randint(0, 10) for i in range(n1)]
# b = [r.randint(0, 10) for i in range(n2)]
# print("a = ", a)
# print("b = ", b)
# c = a + b
# print("c = ", c)

# c = []
# print('Список без повторений: ')
# for i in a:
#     if i not in c:
#         c.append(i)
# for i in b:
#     if i not in c:
#         c.append(i)
# print('Список без повторений: ', c)

# c = []
# for i in a:
#     if i in b and i not in c:
#         c.append(i)
# print('Общие эл-ты: ', c)

# c = [min(a), min(b), max(a), max(b)]
# print(c)

# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
#
# # print(m)
# # print(len(m))
# # print(len(m[1]))
# # print(m[0][1])
# for row in range(len(m)):
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t\t")
#     print()
# print()
#
# for row in m:
#     for x in row:
#         print(x, end="\t\t")
#     print()

# a = [1,2,3]
# print(a)
# for i in a:
#     print(i, end='\t\t')

# a = [[1, 2], [3, 4], [5, 6], [7, 8]]
# print(a)
#
# for x, y in a:
#     print(x, "+", y, "=", x + y)

# m = [[r.randint(0, 10) for i in range(8)] for y in range(4)]
# for row in m:
#     for x in row:
#         print(x, end='\t\t')
#     print()
#
#     # print(row, end='\t\t')
# size = int(input("Размер поля: "))
# symbol = int(input("Кол-во символов: "))
# size = 5
# symbol = 3
#
# i = 0
# while i < size:
#     j = 0
#     while j < symbol:
#         n = 0
#         while n < size:
#             m = 0
#             while m < symbol:
#                 if (i + n) % 2 ==0:
#                     print("+", end='')
#                 else:
#                     print(' ', end='')
#                 m +=1
#             n +=1
#         print()
#         j += 1
#     i += 1

import math

# num1 = math.sqrt(16)
# num2 = math.ceil(3.1)
# num3 = math.floor(3.8)
#
# print(num1)
# print(num2)
# print(num3)
# print(dir(math))
# print(math.pi)

# rd = int(input("Введите радиус: "))
# print("Длинна окружности: ", round(2 * math.pi * rd, 2))

import time
from calendar import month
from itertools import count
from random import random
from time import localtime

# seconds = time.time()
# print("Секунд с начала эпохи", seconds)
# local_time = time.ctime(seconds)
# print(local_time)
# print(2026*365*24*60*60)
# res = time.localtime()
# print("Местное время", res)
# print(res.tm_mday, ":", res.tm_mon,":", res.tm_year, sep='')
# print(time.strftime("TODAY IS %d %B %y"))
# print(time.strftime("%m/%d/%Y, %H:%M:%S",time.localtime(8845696545)))

# pause = 5
# print("START")
# time.sleep(pause)
# print("STOP, seconds: ", pause)

# text = input("Введите напоминание: ")
# local_time = float(input("Через сколько минут: "))
# local_time = local_time * 60
# time.sleep(local_time)
# print(text)

# start = time.time()
# time.sleep(5)
# finish = time.time()
# res = finish - start
# print(res,"sec")
#
# start = time.monotonic()
# time.sleep(5)
# res = time.monotonic() - start
# print(res,"sec")

# import locale
# from tkinter.font import names
#
# from fontTools.misc.cython import returns
# from fontTools.subset.svg import xpath
# from pyparsing import oneOf
#
# locale.setlocale(locale.LC_ALL, "ru")

# print(time.strftime("Сегодня %d %B %y"))
# print(time.strftime("%m/%d/%Y, %H:%M:%S",time.localtime(8845696545)))

# print()

# def hello(name):
#     print("HELLO:", name)
#
#
# hello("Васька")
# hello("Мурзик")

# def get_sum(a, b):
#     print(a + b)
#
#
# get_sum(2, 3)
# x = 5
# y = 6
# get_sum(x, y)
# n = 51
# m = 68
# get_sum(n, m)
# get_sum("asd", "wqeqwe")
# get_sum(2.5, 9.7)

# def symbol(a , b , c):
#     for i in range(a):
#         if i % 2 == 0:
#             print(b, end='')
#         else:
#             print(c, end='')
#     print()
#
# symbol(9, "=", "+")
# symbol(9, 0, 1)

# def get_sum(a, b):
#     # print(a + b)
#     return a + b
#
#
# # get_sum(1,3)
#
# res = get_sum(2, 5)
# print(res)
# print(get_sum(22, 51))

# def maximum(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
# print(maximum(29, 19))

# x = int(input("a: "))
# y = int(input("b: "))
#
# def rs(a, b):
#     if a > b:
#         return a - b
#     else:
#         return a + b
#
# print(rs(x, y))
#
# def cube(a):
#     return a ** 3
#
# for i in range(1, 11):
#     print(i, "в кубе = ", cube(i))

# def fib(n):
#     a = 0
#     b = 1
#     while a < n:
#         print(a, end=" ")
#         c = a + b
#         a = b
#         b = c
#
# fib(15)

# def is_freater(x, y):
#     if x >y:
#         return True
#     else:
#         return False
#
# print(is_freater(10, 3))
# print(is_freater(10, 30))


# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if 'A'<= ch <='Z':
#             has_upper = True
#         elif 'a'<= ch <='z':
#             has_lower = True
#         elif '0'<= ch <='9':
#             has_num = True
#
#     if has_upper and has_lower and has_num:
#         if len(password) >= 8 and has_upper and has_lower and has_num:
#             return True
#         else:
#             if len(password) < 8:
#                 print("Слишком маленький пароль")
#     else:
#         print("Недостаточно требуемых символов")
#     return False
#
# p = input("Введите пароль")
# if check_password(p):
#     print("Пароль надежный")
# else:
#     print("ПАРОЛЬ НЕНАДЕЖНЫЙ")

# def get_sum(a, b, c, d):
#     return a + b + d
#
#
# print(get_sum(1, 4, 8))
# # print(get_sum(1, 4, 6))

# def get_sum(a=4, b=5, c=7, d=9):
#     return a + b + c + d
#
# # print(get_sum(d=1))
# o = 900
# print(get_sum(1, 4,d=o,c=6))

# def sumbol(elements=20, sign='-'):
#     for i in range(elements):
#         print(sign, end='')
#     print()
#
# sumbol(10, '+')
# sumbol(6, '*')
# sumbol(16, '#')
# sumbol(7)
# sumbol()

# def digits_sum(n, vent=True):
#     s = 0
#     while n > 0:
#         curl_digit = n % 10
#         if vent and curl_digit % 2 == 0:
#             s += curl_digit
#         elif not vent and curl_digit % 2 != 0:
#             s += curl_digit
#         n //= 10
#     return s
#
#
# print("СУММА четных")
# print(digits_sum(9874023))
# print(digits_sum(38271))
# print(digits_sum(123456789))
# print("СУММА нечетных")
# print(digits_sum(9874023, False))
# print(digits_sum(38271, False))
# print(digits_sum(123456789, False))

# def display_info(name, age):
#     print("Name: ", name, '\nAge: ', age)
#     print('*' * 50)
#
#
# # display_info("Васька", 3)
# # display_info(3, "Васька")
# display_info(name="Васька", age=3)
# display_info(age=3, name="Васька")
# display_info('Мурка', age=3, name="Васька")

# lst1 = [1,2,3]
# lst2 = [1,2,3]
# lst2 = lst1
# # print(lst1 == lst2)
# # print(lst1 is lst2)
# # print(id(lst1))
# # print(id(lst2))
#
# lt3 = 5
# lt4 = 5
# print(lt3 == lt4)
# print(lt3 is lt4)
# print(id(lt3))
# print(id(lt4))
#
# lst1 = [1,2,3]
# print(id(lst1))
# lst1.append(4)
# print(id(lst1))
# lst1.pop(1)
# print(lst1)
# print(id(lst1))

# s = "Hello"
# print(id(s))
# s += ' World'
# print(s)
# print(id(s))

# a = "HELLO"
# b = "HELLO"
# print(a == b)
# print(a is b)
# print(id(a))
# print(id(b))

# a = True
# b = True
# print(a == b)
# print(a is b)
# print(id(a))
# print(id(b))


# def add_numbers(n):
#     print("Внутри функции", n ,'=', id(n))
#     n +=1
#     print("После изменения", n ,'=', id(n))
#
# x = 1
# print(x ,'=', id(x))
# add_numbers(x)
# print('-' * 50)
# x = add_numbers(x)
# print(x ,'=', id(x))

# def add_numbers(n):
#     print("Внутри функции", n ,'=', id(n))
#     # n += [4]
#     n = n + [4]
#     print("После изменения", n ,'=', id(n))
#
# x = [1,2,3]
# print(x ,'=', id(x))
# add_numbers(x)
# print('-' * 50)

# Типы данных
# Изменяемые: списки(list)
# Неизменяемые: числа(int, float), строки(str), булевы значения(bool), кортеж(tuple)

# lst = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# tpl = (10, 20, 30, 40, 50, 60, 70, 80, 90)
#
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# a = (1, 3, 5, 7, 9)
# print(a)
# print(type(a))
# b = tuple((1, 3, 5, 7, 9))
# print(b)
# print(type(b))
# q = 1
# q = 1,
# q = 1, 2 ,3 ,4 ,"q" # упаковка кортежа
# t = (1)
# t = (1,)
# # print(tuple(q))
# print(tuple(t))

# t1 = tuple('hello')
# print(t1)
# print(t1[1])
# print(t1[1:3])
# t1[1] = 'i'

# lst = [1, 2, 3, 4, 5, 6]
#
# # s1 = [int(input("--> ")) for i in range(5)]
# # s2 = tuple([int(input("--> ")) for i in range(5)])
# # s2 = tuple(int(input("--> ")) for i in range(5))
# s2 = tuple(lst)
# # print(s1)
# print(s2)

# s = input("-> ")
# s = int(input("-> "))
# print(tuple(s))

# mas = [r.randint(0, 100) for i in range(10)]
# tpl = tuple(mas)
# print(tpl)
# mas = [r.randint(0, 100) for i in range(10)]
# print(mas)

# s = tuple(2 ** i for i in range(1, 13))
# print(s)

# t1 = tuple("hello")
# t2 = tuple(" world")
# t3 = t1 + t2
# print(t3)
#
# # print(len(t3))
# # print(t3.count('l'))
# # print(t3.count('a'))
# # print(t3.index('l'))
# # print(t3.index('l', 4))
# # print(t3.index('a'))
# #
# # if "a" in t3:
# #     print(t3.index('a'))
# # else:
# #     print("Элемента нет")
#
# for i in t3:
#     print(i, end=" ")


# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1) + 1
#             return tpl[first: second]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return ()
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# t = (10,11,[1,2,3],[4,5,6],["Hello", "world"])
# print(t, id(t))
# t[4][0] = 'new'
# t[4].append('hi')
# print(t, id(t))

# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t # Распаковка кортежа
#
# print(t)
# print(x, y, z)
# print(type(x))
# print(type(t))

# def get_user():
#     name= "Tom"
#     age = 23
#     is_maried = False
#     return name, age, is_maried
#
# user1, user2, user3 = get_user()
# print(user1)
# print(user2)
# print(user3)
# print(get_user())

# t = (1, 2, 3, 4, 5)
# del t
# print(t)

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# print(type(lst))
# print(lst)
# tpl = tuple(lst)
# print(type(tpl))
# print(tpl)
# print(list(tpl))

# countries = (
#     ("Индия", 1.500,(("Ньд-Делли", 200),("Бангалор", 100))),
#     ("Китай", 3.500,(("Пекин", 500),("Хай-Нань", 150)))
# )
#
# print(countries)
#
# # for country in countries:
# #     print(country)
#
# for country in countries:
#     country_name, country_population, cities = country
#     print("Страна:", country_name, ",население:", country_population)
#     for city in cities:
#         city_name, city_population = city
#         print("Город:", city_name, ",население:", city_population)

# Множества (set) - неупорядоченная коллекция, которая хранить только уникальные значения
#
# {}
# set()

# s = {4,4,5,6,2,2,3,7,8,6,0,2}
# print(type(s))
# print(len(s))
# print(s)

# s = []
# s = ()
# s = {}
# s = set()
# s = set("Hello")
#
#
# print(s)
# print(type(s))

# c = [1, 3, 3, 6, 6, 6, 8, 9, 0, 4]
# s = set(c)
# print(s)
# c = list(s)
# print(c)

# s = {x * x for x in range(10)}
# print(s)

# numbers = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,6,6,6,6,6,6]
# # s = {x for x in numbers if x % 2 == 0}
# s = list({x for x in numbers if x % 2 == 0})
#
# print(s)
#
# def to_set(el):
#     # st = set(el)
#     # return st, len(st)
#     return set(el), len(set(el))
#
#
# print(to_set("я обычная строка"))
# print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))


# {i for i in последовательность}
# {i for i in последовательность if условие}
# {i(True) if условие else i(False) for i in последовательность}
# {i(True) if условие else i(False) for i in последовательность if условие}


# r = ["ab_1", "ac_1", "bc_1", "bc_2"]
# print(r)
# a = {i for i in r}
# print(a)
# a = {i for i in r if "a" not in i}
# print(a)
# #Тернарные выражения
# a = {"A" + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r}
# print(a)
# a = {"A" + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r if i[1] == 'c'}
# print(a)


# a = {'Tom', "Jerry", "Guffy"}
# a.add("Micky")
# print(id(a))
# print(a)
# a.remove("Tom")
# # a.remove("Tom1")
# print(id(a))
# print(a)

# b = "Tom1"
# if b in a:
#     a.remove(b)
# print(a)
# a.discard('Tom1') #Удаляет только если элемент есть, если элемента нет то не выбрасывает исключение
# a.pop() #Удаляет один какой-то элемент
# a.clear()
# print(a)

# # a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
#
# # c = a.union(b)
# # c =  a | b
# # a.update(b)
# # a |= b
# # c = a.intersection(b)
# # c =  a & b
# # a.intersection_update(b)
# # a &= b
# # c = a.difference(b)
# # c = b - a
# # c = a.symmetric_difference(b)
# # c = a ^ b
# # a ^= b
# a = {1, 2}
# # c = a.issubset(b)
# # c = a <= b
# # c = a.issuperset(b)
# # c = a>= b
#
# print("a = ", a)
# print("b = ", b)
# print("-" * 25)
# print(c)

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
#
# # s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# s = s1.union(s2, s3, s4, s5, s6, s7)
# print(s)
# print(len(s))
# print(min(s))
# print(max(s))

# s1 = "Hello"
# s2 = "How are you"
# a = set(s1) & set(s2)
# print(a)
# for i in a:
#     print(i, end=" ")

# drawing = {"Marina","Jenya","Sveta"}
# music = {"Kostya","Jenya","Ilya"}
#
# one = drawing ^ music
# print(one)
#
# two = drawing & music
# print(two)
#
# drawing = drawing - two
# print(drawing)

# Тип frozenset(замороженное множество)

# a = frozenset([5, 6, 7, 8, 9, 1, 2, 3, 4])
# print(a)
#
# s1 = set("hello")
# print(s1)
# s = frozenset("hello")
# print(s)


# Словарь dict() - изменяемый тип данных. Данные храняться по принципу ключ значение

# lst = ['one', 'two', "three"]
# print(lst)
# print(lst[0])

# d = {"a": 'one', "b": 'two', "c": "three", "aa": 'one'}
# print(d)
# print(d['b'])

# d = {}
# print(d)
# print(type(d))

# d = {"one": 1, 2: "two"}
# print(d)

# users = ['ivan@gmail.com', "Ivan"]
# users = [['ivan@gmail.com', "Ivan"]]
# users = [
#     ['ivan@gmail.com', "Ivan"],
#     ['anna@gmail.com', "Anna"],
#     ['julie@gmail.com', "Julie"],
# ]
#
# print(users)
# d_users = dict(users)
# print(d_users)

# d = {i for i in range(7)}
# print(d)

# d = {i: i for i in range(7)}
# d = {i: i ** 2 for i in range(7)}
# print(d)
# print(d[2])
# d[2] = 99
# d[9] = 9 ** 2
# print(d)
#
# d = {0: 'text', "one": 17, (1, 2.3): "Кортеж",33: [1, 2, 3], True: 11}
# # print(d)
# # print(d[33][2])
# # print(d[(1, 2.3)])
#
# # print("one" in d)
# # print("two" in d)
#
# # print(d["two"])
#
# # key = "one"
# # # key = "two"
# #
# # # del d[key]
# #
# # # if key in d:
# # #     del d[key]
# #
# # try:
# #     del d[key]
# # except KeyError:
# #     print('Нет такого элемента')
# #
# # print(d)
#
# for key in d:
#     print(key,"->", d[key])


# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# res = 1
# for key in d:
#     res *= d[key]
#
# print(res)

# d = {}

# d[1] = input('->')
# d[2] = input('->')
# d[3] = input('->')
# d[4] = input('->')

# d = {i: input('-> ') for i in range(1, 5)}
#
# print(d)
# dislike = int(input("Что удалить: "))
# del d[dislike]
# print(d)
#
# goods = {
#     "1": ["Core-i3-4330", 9, 4500],
#     "2": ["Core-i5-4670K", 3, 8500],
#     "3": ["AMD FX-6300", 6, 3700],
#     "4": ["Pentium G3220", 8, 2100],
#     "5": ["Core-i5-3450", 5, 6400],
# }
#
# for i in goods:
#     print(i, ")", goods[i][0], ' - ', goods[i][1], " шт. по ", goods[i][2],"руб.", sep='')
#
# while True:
#     n = input('№')
#     if n != "0":
#         k = int(input("Количество: "))
#         goods[n][1] = k
#     else:
#         break
#
# for i in goods:
#     print(i, ")", goods[i][0], ' - ', goods[i][1], " шт. по ", goods[i][2],"руб.", sep='')

# d = {"A": 1, "B":2, "C":3}
# v = d["B"]
# print("B = ",v)

# value = d.get('B')
# value = d.get('E')
# value = d.get('A', "False")
#
# print(value)
# d.clear()
# print(d)

# d2 = d.copy()
# d2 = d
# print('D = ', d)
# print('D2 = ', d2)
# print()
#
# d['E'] = 9
# d2["W"] = 77
#
# print('D = ', d)
# print('D2 = ', d2)

# d = {"A": 1, "B":2, "C":3}
# a = d.items()
# a = d.keys()
# a = d.values()
# print(a)
# print(d["A"] + d["C"])

# for key in d.keys():
#     print(key,end=' ')

# for key in d.values():
#     print(key, end=' ')

# for key in d.items():
#     print(type(key), end=' ')

# for key, val in d.items():
#     print("key = ", key, ".valoue = ",val)

# d = {"A": 1, "B": 2, "C": 3}

# item = d.pop("B")
# item = d.pop("E")
# item = d.pop("E", "NOT FOUND")
#
# print(item)
# print(d)

# item = d.setdefault("C")
# item = d.setdefault("E")
# item = d.setdefault("B", 5)
# print(item)
# print(d)

# d.update([("E", 5),("F", 55),("V", 55)])
# d.update([("E", 5)])
# print(d)

# x = {'a':1, 'b':2}
# y = {'b':3, 'c':4}
# # z = x |y
# z = x.copy()
# z.update(y)
# print(z)

# d = {'name': "Kelly", "age":25, "salary":8000, 'city': "New York"}
#
# new_d = dict()
# new_d['name'] = d.pop('name')
# new_d['salary'] = d.pop('salary')
#
#
# print(d)
# print(new_d)

# Вложенные словари
#
# a = {
#     'First': {
#         1: "one",
#         2: "two",
#         3: "three"
#     },
#     'Second': {
#         4: "four",
#         5: "five",
#     }
# }
#
# # print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print(y," ", a[x][y], sep='')

# sales = {
#     "John": {"N": 3056,"S":8463,"E":8441, "W":2694},
#     "Tom": {"N": 4832,"S":6786,"E":4737, "W":3612},
#     "Anne": {"N": 5239,"S":4802,"E":5820, "W":1859},
#     "Fiona": {"N": 3904,"S":3645,"E":8821, "W":2451},
# }
#
# for x in sales:
#     print(x)
#     for y in sales[x]:
#         print(y," ", sales[x][y], sep='')
#
# person = input("Имя: ")
# region = input("Регион: ")
# print(sales[person][region])
# data  = int(input("Новое значение: "))
# sales[person][region] = data
# print(sales[person])

# data = {"один": 1, "два": 2, "три": 3, "четыре": 4}
# d = {k: v for k, v in data.items()}
# print(d)
# data["один"] = 99
# print(data)
# print(d)

# data = {"один": 1, "два": 2, "три": 3, "четыре": 4}
# d = {k: v for k, v in data.items() if v <= 2}
# print(d)

# s = "Hello"
# b = {i: i * 3 for i in s}
# print(b)
#
# # a = list(b)
# a = list(b.items())
#
# print(a)


# a = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
#
# d = dict()
# s = None
# for i in a:
#     if type(i) == str:
#         d[i] = []
#         s = i
#     else:
#
#         d[s].append(i)
# print(d)


# zip() #Создает словарь из двух списков
#
# d = zip([1, 2, 3], ["Январь", "Февраль", "Март"])
# d = dict(zip([1,2,3],["Январь","Февраль","Март"]))
#
# print(d)
# print(type(d))
# # print(dict(d))
# print(list(d))

# a = ["Январь", "Февраль", "Март"]
# b = [1, 2, 3]
# d = {k: v for k, v in zip(b, a)}
#
# print(d)

# b = [12, 1, 6]
# c = zip(b)
# # print(list(c))
# print(dict(c))


# a = ['a', 'b', 'd', 'c']
# b = [12, 1, 6]
# c = [2.3, 5.6, 1.0]
# q = zip(a, b, c)
# # print(list(q))
# print(dict(q))

# print(list(zip(range(100), range(600))))
# students = {}
# students_value = int(input("кол: "))
# marks = 0
# for i in range(students_value):
#     number = input("Студент: ")
#     mark = int(input("Баллы: "))
#     students[number] = mark
#     marks += mark
#
# average = marks / students_value
# print("Средний", average)
# for i in students:
#     if students[i] > average:
#         print(i)

# one = {"name":"Иван","last_name":"Петров","job":"Консультант"}
# two = {"name":"Петр","last_name":"Иванов","job":"Менеджер"}
#
# for (k1,v1), (k2,v2) in zip(one.items(), two.items()):
#     print(k1, "->", v1)
#     print(k2, "->", v2)

# Распаковка последовательности
# pairs = [(1,"a"),(2,"b"),(3,"c"),(4,"d")]
# print(pairs)
# a, b = zip(*pairs)
# print(a)
# print(b)


# month = ["Январь", "Февраль", "Март"]
# total_sales = [52000.00, 51000.00, 48000.00]
# prod_cost = [46800.00, 45900.00, 43200.00]
#
# for sales, costs, m in zip(total_sales, prod_cost, month):
#     profit = sales - costs
#     print("Общая прибыль в ", m, '=', profit)

# one = {"apple": 20, "orange": 35, "peper": 60}
# two = {"peper": 40, "onion": 55}
# print(one, two)
# print([one, two])
# print({**one, **two})


# for i in range(3):
#     print(i)

# color = ["red", 'yellow', "green"]
# j = 1
# for i in color:
#     print(j, i)
#     j +=1


# enumerate(iterable, start=0):

# color = ["red", 'yellow', "green"]
#
# for j,i in enumerate(color, 1):
#     print(j, i)

# num_list = [1, 2, 3, 4, 5]
# i = iter(num_list)
# # print(i)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i, "STOP"))
# print(next(i, "STOP"))

# a = [1, 2, 3]
# b = [*a ,4, 5, 6]
# # print(b)
#
#
# # def func(c):
# #     return c
#
# def func(*args):
#     return args
#
# print(func(2,3,4))
# print(func())

# def summa(*param):
#     rez = 0
#     for i in param:
#         rez += i
#     return rez


# print(summa(1, 3))
# print(summa(1, 3, 5, 6, 89, 9, 23, 234, 64, 7, 23, 24, 46, 4334, 5))


# def to_dict(*args):
#     return {i: i for  i in args}
#
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict("grey", (2, 17), 3.11, -4))

# def ch(*args):
#     res = []
#     sr_ar = sum(args) / len(args)
#     print(sr_ar)
#
#     for i  in args:
#         if i < sr_ar:
#             res.append(i)
#     return res
#
#
# print(ch(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(ch(3, 6, 1, 9, 5))

# def func(b, *args):
#     return b , args
#
# print(func(1))
# print(func(1,2,3,4,"hello"))


# def print_score(name, *scores):
#     print("Имя студента " + name)
#     for score in scores:
#         print(score)
#
#
# print_score("Ivan", 100, 95, 88, 92, 90)
# print_score("Igor", 96, 20, 33)

# def func(**kwargs):
#     return kwargs
#
#
# print(func())
# print(func(a=1, b=2, c=3))
# print(func(a="python"))
# print(func(_2="python"))

# def intro(**data):
#     for key, value in data.items():
#         print(key, "is", value)
#     print()
#
# intro(first_name="Agatha", last_name="Cristi", age=22)
# intro(first_name="Igor", last_name="Ivanov",email ="igor@gmail.com", age=92, phone = "999-99-999-99")

# def db(**kwargs):
#     my_dict.update(kwargs)
#
#
# my_dict = {'one': "firs"}
# db(k1=22, k2=31, k3=91)
# db(name="Bob", age=31, weigth=61, eyes_color="grey")
# print("my_dict = ", my_dict)


# def db(b, c, w,*args, a, name,  **kwargs):
#     print(b, c, w, a, args, name, kwargs)
#
#
# db(4, 8, 1, 1,2, a=4, name="Anna", q=4)

# Области видиммости(всего 4)


# name = "Tom"
#
# def hi():
#     name = "Jerry" #Локальная
#     print("Hello", name)
#
#
# def bye():
#     print("Good bye", name)
#
# hi()
# bye()
# print(name)

# name = "Tom"
#
# def hi():
#     global name
#     name = "Jerry" #Локальная
#     print("Hello", name)
#
#
# def bye():
#     print("Good bye", name)
#
# print(name)
# # hi()
# bye()
#
# name = "Sam"
# print(name)


# def topk(nums, k):
#     count = {}
#     for num in nums:
#         if num in count:
#             count[num] +=1
#         else:
#             count[num] = 1
#     items = []
#     for num, val in count.items():
#         items.append((num, val))
#
#     def get_freq(pair):
#         return  pair[1]
#     items.sort(key=get_freq, reverse=True)
#
#     result = []
#     for i in range(k):
#         result.append(items[i][0])
#
#     return result
#
#
#
# nums = [1,1,1,2,2,3,3,3,3,3,3,3,3,4,4,4,4,5,5,5,5,]
# k=3
# print(topk(nums,k))


# name = "Tom"
#
# def hi():
#     global name
#     name = "Jerry" #Локальная
#     print("Hello", name)
#
#
# def bye():
#     print("Good bye", name)
#
# print(name)
# # hi()
# bye()
#
# name = "Sam"
# print(name)

# i = 5
#
#
# def func(arg=i):
#     print("i =", i)
#     print("arg =", arg)
#
# i = 6
# func()

# x = 4
#
# def add_two(a):
#     # x = 2
#
#     def add_some():
#         # x = 5
#         print('x =', x)
#         return a + x
#     return add_some()
#
# print(add_two(3))

# import builtins
#
# names = dir(builtins)
#
# for t in names:
#     print(t)

# min = [4, 5, 6]
# print(max(min))
# print(min(min))


# def outer_func(who):
#     def inner_func():
#         print("Hello,", who)
#
#     inner_func()
#
# outer_func('World!')


# a = 2
# def func1():
#     a = 6
#     def func2(b):
#         global a
#         a = 4
#         print("Сумма", a + b)
#     print('a = ', a)
#     func2(4)
#
#
# print("Global1 ",a)
# func1()
# print("Global2 ",a)

# def fn1():
#     x = 25 # 1
#
#     def fn2():
#         nonlocal x
#         x = 33 # 3
#
#         def fn3():
#             nonlocal x
#             x = 44 # 5
#             print("fn3.x =",x) # 6
#         fn3() # 4
#         print("fn2.x =", x) # 7
#     fn2() # 2
#     print("fn1.x =", x) # 8
#
# fn1()

# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return a, b
#
# res = outer(2, 3, -1, 4)
# print(res)


# def increment(number):
#     def inner():
#         return number + x
#     return inner()
#
# print(increment(12))

# def increment(number):
#     print("number =", number)
#     def inner(x):
#         print("x =",x)
#         return number + x
#     return inner
#
# # a = increment(12)
# # # print(a)
# # print(a(5))
# # print(a(2))
# # print("-"*23)
# # b = increment(1)
# # # print(a)
# # print(b(6))
# # print(b(10))
#
# print(increment(10)(5))

# def func1():
#     a = 1
#     b = "line"
#     c = [1, 2, 3]
#
#     def func2():
#         return a, b, c
#     return func2
#
# # func = func1()
# # print(func())
# print(func1()())

# def func1():
#     a = 1
#     b = "Hello"
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a + 1
#         b = b + '_World!'
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
#     return inner
#
# res1 = func("Москва")
# res1()
# res1()
#
# res2 = func("Сочи")
# res2()
# res2()
# res2()
# res1()
# res1()
#
# student = {
#     "Иван":96,
#     "Антон":45,
#     "Анна":88,
#     "Валерий":76,
#     "Катя":49,
#     "Настя":30,
#     "Дима":54,
#     "Маша":66,
#     "Яна":77,
#     "Васька":88,
# }
#
# def make_classife(lower, upper):
#     def students(exam):
#         return {k: v for k,v in exam.items() if lower<= v < upper}
#     return students
#
# a = make_classife(80, 100)
# b = make_classife(70, 80)
# c = make_classife(50, 70)
# d = make_classife(0, 50)
#
# print("5", a(student))
# print("4", b(student))
# print("3", c(student))
# print("2", d(student))


# lambda - анонимные функции
#
# def get_sum(x, y):
#     return x + y
#
#
# print(get_sum(1, 2))
# print(get_sum(3, 4))
# print("-" * 20)
#
# print((lambda x, y: x + y)(1, 2))
# print((lambda x, y: x + y)(3, 4))

# func = lambda x, y: x + y
# print(func(1, 2))
# print(func(3, 4))

# print((lambda x, y: x ** 2 + y ** 2)(2, 5))

# summ = lambda a=1, b=2, c=3: a + b + c
# #
# # print(summ()) #6
# # print(summ(10)) #15
# # print(summ(10,20)) #33
# # print(summ(10,20, 30)) #60

# func1 = lambda *args: args
#
# print(func1(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(func1('a', 'b', 'c', 'd'))

# c = (
#     lambda x:x*2,
#     lambda x:x*3,
#     lambda x:x*4
# )
#
# for t in c:
#     print(t('abc_'))

# def inc(n):
#     def inner(x):
#         return n + x
#     return inner
#
# f = inc(5)
# print(f(2))

# def inc(n):
#     return lambda x: n + x
#
# f1 = inc(5)
# print(f1(2))
#
# inc2 = lambda n: lambda x: n+x
#
# f2 = inc2(5)
# print(f2(2))


# print((lambda n: lambda x: n+x)(5)(2))


# print((lambda n: lambda x: lambda y: n+x+y)(5)(2)(3))

# d = {'b':10,'a':15,'c':32}
#
# # d.sort
# # print(sorted(d.items()))
#
# list_d = list(d.items())
# print(list_d)
# list_d.sort()
# print(list_d)
#
# list_d.sort(key=lambda i: i[1], reverse=True)
# print(list_d)
# print(dict(list_d))

# players = [
#     {'name': "Антон", "last name": "Бирюков", "rating": 9},
#     {'name': "Алексей", "last name": "Бодня", "rating": 10},
#     {'name': "Федор", "last name": "Сидоров", "rating": 4},
#     {'name': "Михайл", "last name": "Семенов", "rating": 6}
# ]
#
# res1 = sorted(players, key=lambda items: items["last name"])
# print(res1)
#
# res2 = sorted(players, key=lambda items: items["rating"], reverse=True)
# print(res2)
#
# res3 = sorted(players, key=lambda items: items["rating"])
# print(res3)

# a = [(lambda x, y: x + y), (lambda x, y: x - y), (lambda x, y: x * y), (lambda x, y: x / y)]
#
# b = a[0](5, 3)
# print(b)

# d = {
#     1: lambda: print("Понедельник"),
#     2: lambda: print("Вторник"),
#     3: lambda: print("Среда"),
#     4: lambda: print("Четверг"),
#     5: lambda: print("Пятница"),
#     6: lambda: print("Суббота"),
#     7: lambda: print("Воскресенье"),
# }
#
# # print(d[1])
# d[3]()


# print((lambda a, b: a if a > b else b)(15, 2))

# map(func, *iterable)

# def mult(t):
#     return t * 2
#
#
# lst = [2, 7, 4, -4, 10, -7]
#
# a = list(map(mult, lst))
#
# print(a)
#
# print(list(map(lambda t: t * 2, lst)))

# b = ['1', '2', '3', '4', '5']
# print(b)
# c = list(map(int, b))
# print(c)
# print(type(c))

# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5, 6, 7]
#
# print(list(map(lambda x, y: (x, y), num, st)))
# print(list(map(lambda x, y: {x: y}, num, st)))
# print(list(map(lambda x, y: str(x) + y, num, st)))

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
#
# print(list(map(lambda x, y: x + y, l1, l2)))

# res = filter(func => (true or false), *iterable)

# t = ('abc', "abcd", "def", 'tres', "ufo", 'lopp')
#
# t2 = tuple(filter(lambda s: len(s) == 4, t))
# print(t2)

# b = [55, 77, 32, 89, 94, 45, 22, 99, 26, 56, 45, 50]
# res = list(filter(lambda s: s < 50, b))
# print(res)

# import random
#
# lst = [random.randint(1,40) for i in range(10)]
#
# print(lst)
#
# res = list(filter(lambda x: 10 <= x <= 20, lst))
# print(res)

# def hello():
#     return "Hello, I am func 'hello'" #3
#
# def bye():
#     return "BYE!!!"
#
# def super_func(func):
#     print("Hello, I am 'super_func'") #2
#
#     print(func()) #4
#
#
# # super_func(hello) #1
# super_func(bye) #1


# def hello():
#     return "Hello, I am func 'hello'"
#
# test = hello
# print(test())

# def my_decorator(func): #2
#     def func_wrapper(): #3
#         print("Code before")#4
#         func()#5
#         print("Code after")#8
#     return func_wrapper #3
#
#
# def func_test(): #6
#     print("func_test") #7
#
# text = my_decorator(func_test) #1
# text()
#
# def my_decorator(func):
#     def func_wrapper():
#         print("*" * 40)
#         func()
#         print("=" * 40)
#     return func_wrapper
#
#
# @my_decorator
# def func_test(): #6
#     print("func_test") #7
#
#
# func_test()
#
# @my_decorator
# def hello():
#     print('hello')
#
# hello()

# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#     return wrap
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#     return wrap
#
# @bold
# @italic
# def hello():
#     return "text"
#
# print(hello())

# def cnt(fn):
#     count = 0
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print("Вызов функции", count)
#     return wrap
#
#
# @cnt
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()

# def args_decorator(fn):
#     def wrap(args1, args2):
#         print("Данные", args1, args2)
#         fn(args1, args2)
#     return wrap
#
#
# @args_decorator
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#
#
# print_full_name("Иван", "Петров")

#
# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print("args", args)
#         print("kwargs", kwargs)
#         fn(*args, **kwargs)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(a, b, c, study='С#'):
#     print(a, b, c, "изучают", study)
#
#
# print_full_name("Иван", "Петр", "Борис", study="Python")
# print_full_name("Васька", "Мурзик", "Мурка")

# def args_dec(fn):
#     def wrap(x, y):
#         print("Сложение", x, "и", y, '=', end=' ')
#         fn(x, y)
#
#     return wrap
#
#
# @args_dec
# def summa(a, b):
#     print(a + b)
#
#
# @args_dec
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)

# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, '=', end=' ')
#             fn(x, y)
#         return wrap
#     return args_dec
#
#
# @decor("Сложение", "+")
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность", "-")
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)
#
# def myltiply(arg):
#     def my_decorator(func):
#         def wrap(*args, **kwargs):
#             return arg * func(*args, **kwargs)
#
#         return wrap
#
#     return my_decorator
#
#
# @myltiply(5)
# def return_num(num):
#     print("num = ", num)
#     return num
#
# @myltiply(10)
# def return_str(s):
#     return s
#
#
# @myltiply(10)
# def summa(a,b):
#     return a + b
#
# print("Resut", return_num(7))
# print("Resut", return_str('a'))
# print("Resut", summa(1,5))

# print(01)
# print(int("10"))
# print(int("1010", 2))
# print(int("12", 8))
# print(int("A", 16))

# print(10)
# print(bin(10)) #0b1010
# print(oct(10)) #0o12
# print(hex(10)) #0xa

# q = "Pyt"
# w = 'hon'
# e = q + w
# # print(e)
# #
# # print(e * 3)
# # print(e * -3)
#
# print(e in "I am learning Python")
# print(e in "I am learning JS")

# s = 'Hello'
#
# # print(s[1])
# # print(s[-5])
# # print(s[5])
# print(s[2:4:])
# print(s[::2])

# s = "python"
# a = s[:3] + 't' + s[4:]
# print(a)


# def chanegChar(s, c_old, c_new):
#     i = 0
#     s2 = ""
#     while i < len(s):
#         if s[i] == c_old:
#             s2 = s2 + c_new
#         else:
#             s2 = s2 + s[i]
#         i += 1
#     return s2
#
#
#
# str1 = "Я изучаю Nython. Мне нравиться Nython. Nython очень интересный язык программирования."
# str2 = chanegChar(str1, "N", "P")
# print(str1)
# print(str2)

# print("Привет")
# print(u"Привет") #utf-8

# print('I\'m learning \n python!')
# print('C:\\file.txt')
# print(r'C:\file.txt')
# print(r'C:\file.txt\\'[:-1])
# print(r'C:\file.txt' + "\\")
# print('C:\\file.txt\\')

# name = "Дмитрий"
# age = 25
#
# print("Меня зовут", name,".","Мне", age,"лет." )
# print(f"Меня зовут {name}. Мне {age} лет." )

# import  math
#
# print(f"Значение числа pi: {round(math.pi, 2)}")
# print(f"Значение числа pi: {math.pi:.2f}")

# x = 10
# y = 5
#
# print(f"{x} x {y} / 2 = {x * y / 2}")

# a = 74
# print(f"{{{{{a}}}}}")
#
# dir_name = "my_doc"
# file_name = "data.txt"
#
# print(fr"home\{dir_name}\{file_name}")
# # print(f"home\{dir_name}\{file_name}")
# print('home\\' + dir_name + "\\" + file_name)


# s = '''
# <div>
#     <a>Какой-то текст</a>
# </div>
# '''
# print(s)

# def squares(n):
#     """
#     Принимает число n, и возвращает квадрат числа n
#     """
#     a = 2
#     return n ** a
#
# print(squares(5))
# print(squares.__doc__)

# print(ord("c"))
# print(ord("#"))
# print(ord("с"))

# while True:
#     n = input("-> ")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break
#
# my_str = "Test string for me"
# arr = [ord(x) for x in my_str]
# print("ASCII коды: ", arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифметическое: ", arr)
# arr += [x for x in [ord(x) for x in input("-> ")[:3]] if x not in arr]
# print(arr)
# if arr[-1] in arr[:-1]:
#     print("Количество последних элементов: ", arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)
#
# print(chr(114))
# print(chr(1069))
#
# a = 1073
# b = 1103
#
# if a > b:
#     for i in range(b,a + 1):
#         print(chr(i), end=" ")
#     else:
#         for i in range(a, b + 1):
#             print(chr(i), end=" ")


# print("apple" == "Apple")
# print("apple" > "Apple") #97 > 65
#
# from random import randint
#
# short = 8
# longest = 12
# min_ascii = 33
# max_ascii = 126
#
# def random_password():
#     random_length = randint(short, longest)
#     res = ''
#     for i in range(random_length):
#         random_char = chr(randint(min_ascii, max_ascii))
#         res += random_char
#     return res
#
# print("Ваш пароль ", random_password())

# s = "hello, WORLD! I am learn Python"
# print(s.capitalize()) #Hello, world! i am learn python
# print(s.lower()) #hello, world! i am learn python
# print(s.upper()) #HELLO, WORLD! I AM LEARN PYTHON
# print(s.swapcase()) #HELLO, world! i AM LEARN pYTHON
# print(s.title()) #Hello, World! I Am Learn Python

# s = "hello, WORLD! I am learn Python"
#
# # print(s.count('h',1, -4)) #количество искомых символов
# print(s.find('Python')) #возвращает индекс первого вхождения
# print(s.find('рPython')) #если подстроки не, возвращает -1

# string = "один два"
# one = string[:string.find(' ')]
# two = string[string.find(' ') + 1:]
# print(two + " " + one)

# s = "ab12c59p7dq7878978978"
# digits = []
# for symbol in s:
#     if "0123456789".find(symbol) != -1:
#         digits.append(int(symbol))
# print(digits)

# for i in range(10):
#     if str(i) in s:
#         digits.append(i)
# print(digits)
#
# s = "hello, WORLD! I am learn Python"
# # print(s.find('Python'))
# # print(s.index("Python"))
# print(s.index("oPython"))

# s = "Дана ст(рока символов, среди которых есть одна открыв)ающаяся"
# ind1 = s.index("(")
# ind2 = s.index(")")
#
# print(ind1)
# print(ind2)
#
# print(s[ind1 + 1:ind2])

# s = "hello, WORLD! I am learn Python"
# # print(s.find('a'))
# # print(s.rfind('a'))
# print(s.index('a'))
# print(s.rindex('a'))

# s = "Lorem consequat"
#
# item = "x"
# if s.count(item) == 1:
#     print(s.find(item))
# elif s.count(item) >= 2:
#     print(s.find(item), s.rfind(item))

# s = "hello, WORLD! I am learn Python"
# print(s.endswith("on"))
# print(s.endswith("lo",3,5))

# print(s.startswith("hello"))
# print(s.startswith("I am", 14))

# print("aabb123".isalnum()) #состоит из букв или цифр
# print("23234&*asdad".isalnum())

# print("ASDFdfssdfsd".isalpha()) # проверяет содержит ли только буквы
# print("ASDFdf1231231ssdfsd".isalpha())
#
# print("1123132".isdigit()) # проверяет содержит ли только цифры
# print("1asd123132".isdigit())


# print("asdasdasd121212".islower()) # проверяет содержит ли только буквы в нижнем регистре также могут быть цифры
# print("asВВВВВasd121212".islower()) #


# print("ВВВВВ121212".isupper()) # проверяет содержит ли только буквы в верхнем регистре также могут быть цифры
# print("ВВВВaaaaВ121212".isupper())


# print(" ".isspace()) # проверяет содержит ли из пробелов или знака табуляции или переноса строки
# print(" a ".isspace())

#
# print("a".center(10))
# print("a".center(11, "-"))

# print("     py")
# print("     py".lstrip())
# print("py            ".rstrip())
# print("         py            ".lstrip())

# print("https://www.python.org/".lstrip("th/ps:"))
# print('$py.$$$;'.rstrip("$;"))
# print('$py.$$$;'.lstrip("$;"))

# str1 = "Я изучаю Nython. Мне нравиться Nython. Nython очень интересный язык программирования."
#
# print(str1.replace("Nython","Python", 1))

# s = '-'
# seq = ('a',"b","c")
# print(s.join(seq))

# print('..'.join(['1','2']))
# print(':'.join({"a":'1',"b":'2'}))

# print("Строка разделенная пробелами".split(" "))
# print("www.python.org.ru".split(".",4))
# print("www.python.org".rsplit(".",1))
# print("www...python...org".rsplit("."))

# a = input("-> ").split()
# print(a)
#
# def name(name):
#     print(f"{name[0]} {name[1][0]}.{name[2][0]}.")
#
# name(a)

# s = "В строке заменить пробелы символом"
# # print(s.replace(" ", "*"))
# ls = s.split()
# print(ls)
# st = "*".join(ls)
# print(st)


import re

# Регулярные выражения
# s = "Я ищу совпадения в 2026 года. И я из найду в 2 счёта."
# reg = 'Я ищу'
# print(s.find(reg))
# print(s.find(reg))

# print(re.findall(reg, s)) # возвращает список содержащий все элементы
# print(re.search(reg, s)) # возвращает первое совпадение
# print(re.search(reg, s).span()) #(15, 16)
# print(re.search(reg, s).start()) #15
# print(re.search(reg, s).end()) #16
# print(re.search(reg, s).group()) #я

# print(re.match(reg, s)) # для поиска по задонному шаблону только с начала строки

# s = "Я ищу совпадения в 2026 года. И я из найду в 2 счёта."
# reg = "я"
# reg = r"\\"

# print(re.split(reg, s))
# print(re.split(reg, s, maxsplit=1))
#
# print(re.sub(reg, "!", s, count=1))


# s = "Я ищу совпадения в 2026 года. И я из найду в 2 счёта. 99798784"
# reg = "206"
# reg = r"[206]"
# reg = r"[0-9]"
# reg = r"[0-9][0-9]"
# reg = r"[0-9][0-9][0-9][0-9]"
# reg = r"[12][0-9][0-9][0-9]"

# [] - любой из символов внутри

# reg = r"[а-я]"
# reg = r"[а-яё]"
# reg = r"[А-Яа-яё]"
# reg = r"[А-яё]"
#
# print(re.findall(reg, s))


# s = "Еда, беду, победа"
# reg = r"[Ее]д[ау]"
# print(re.findall(reg, s))


# s = "Я ищу со[впаден]ия в 2026 го-да. И я из найду в 2 счёта. 456787"
# # reg = r"[А-яё.]"
# # reg = r"[А-яё.]."
#
# reg = r"[А-яё.\[\]-]"
#
#
#
# print(re.findall(reg, s))


# s = "Я ищу совпадения в 2026 го-да. И я из найду в 2 счёта. 99798784"
# reg = r"[^0-9]"
# # [^abc] - вернет все кроме abc
# print(re.findall(reg, s))


# s = "Час в 24-часовом формате от 00 до 23. 2021-06-15Т21:45. Минуты, в диапазоне от 00 до 59. 2021-06-15Т01:09."
# reg = r"[0-2][0-9]:[0-5][0-9]"
#
# print(re.findall(reg, s))


# s = "Я ищу совпадения в 2026 го-да. И_я из \tнайду в 2\n счёта. 99798784"
# reg = r"\S"
# #\d - одна цифра [0-9]
# #\w - одна цифра, буква, символ _ [0-9А-яA-z]
# #\s - пробельный символ (включая табуляцию и перенос стоки)
# #\D - все кроме цифр [^0-9]
# #\W - все кроме цифр, букв, символа _ [^0-9А-яA-z]
# #\S - все кроме пробельного символа (включая табуляцию и перенос стоки)
#
# print(re.findall(reg, s))


# s = "Я ищу совпадения в 2026 го-да. И_я из \tнайду в 2\n счёта. 99798784"
# # reg = r"\AЯ ищу"
# # reg = r"798784\Z"
# # reg = r"Я ищу\b"
# reg = r"8784\B"
#
# print(re.findall(reg, s))


# s = "Я ищу совпадения в 2026 го-да. И_я из \tнайду в 2\n счёта. 9979878999994"
# # reg = r"\w+"reg = r"\w+"
# reg = r"20*"
# #+ - от 1 до бесконечности повторений
# #* - от 0 до бесконечности повторений
# #? - 0 или 1
#
# print(re.findall(reg, s))

# s = "цифры: 7, +17, -42, 0.0.13, 0.3"
# reg = r"[+-]?[\d.]+"
#
# print(re.findall(reg, s))

# s = "05-03-1987 # Дата рождения"
# print("Дата рождения:", re.sub("#.*",'',s))
#
# # 05.03.1987
# print("Дата рождения:", re.sub("-",".", re.sub("#.*",'',s)))

# s = 'author=Пушкин А.С.; title = Евгений онегин; price =200; year= 1831'
# # reg = r"\w+\s*=\s*[^;]+"
# reg = r"[^;]+"
# print(re.findall(reg, s))

# s = "24 марта 2026 года"
# # reg = r"\d\d\d\d"
# reg = r"\d{2,4}"
#
#
# print(re.findall(reg, s))


# s = "+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564478"
# reg = r"\+?7\d{10}"
#
# print(re.findall(reg, s))

# s = "Я ищу совпадения в 2026 го-да. И_я из \tнайду в 2 счё_та"
#
# reg = r"^\w+\s\w+"
# print(re.findall(reg, s))
#
# reg = r"\w+\s\w+$"
# print(re.findall(reg, s))

# print(re.findall(r"\w+", "12 + qe"))
# print(re.findall(r"\w+", "12 + qe", flags=re.ASCII))
# print(re.findall(r"[^А-я]+[0-9]", "12 + йцу"))

# text = "h+ello world"
# print(re.findall(r"\w\+",text, flags=re.DEBUG))


# s = "Я ищу совпадения в 2026 го-да. И_я из \tнайду в 2 счё_та"
#
# reg = "я"
# print(re.findall(reg, s, flags=re.IGNORECASE))
# print(re.findall(reg, s, re.I))

# text = """
# one
# two
# """

# print(re.findall(r"one",text))
# print(re.findall(r"one.\w+",text, flags=re.DOTALL))
# print(re.findall(r"one$",text))
# print(re.findall(r"one$",text, flags=re.MULTILINE))

# print(re.findall("""[a-z.-]+@[a-z.-]+""", "test@gmail.ru", flags=re.VERBOSE))
#
# print(re.findall("""
# [a-z.-]+ #part1
# @       # @
# [a-z.-]+ #part2
# """, "test@gmail.ru", flags=re.VERBOSE)


# text = """Python,
# python,
# PYTHON"""
# # reg = "python"
# # reg = "^python"
# # reg = "(?m)python"
# reg = "(?im)python"
#
# print(re.findall(reg, text))

# ^ $
# def validate_name(name):
#     return re.findall(r"^[\w-]{3,16}$", name ,re.IGNORECASE)
#
# print(validate_name("Python_master"))
# print(validate_name("@Python_master"))
# print(validate_name("Pyth@on_master@"))
# print(validate_name("Python_ma5st&er"))

# text = "<body>Принцип жадности соответствия регулярных выражений</body>"
# print(re.findall("<.*?>",text))

# greedy - захватывает максиммально возможное число символов
# ? - lazy - захватывает минимально возможное число символов
#
# применяется с
# *?, +? , ??
# {m,n}?, {,n}?, {m,}?

# s = "<p> Изображение <img alt='image' src='bg.jpg'> - фоновое изображение </p>"
# # reg = r"<img[^>]*>"
# reg = r"<img\s+[^>]*src\s*=\s*[^>]+>"
#
# print(re.findall(reg, s))
# text = "Microsoft Edge удаляет журнал браузера[16], файлы cookie и данные сайтов, а также пароли, адреса и данные ф[17]орм при закрытии всех окон InPrivate. Другие люди, использующие это устройство, не увидят ваши действия по просмотру веб-страниц, но к этим данным все же, вероятно, смогут получить[18][19] доступ учебное заведение, работодатель и поставщик услуг Интернета."
# print(re.findall(r"\[.*?]", text))

# s = "Вася, Маша, Даша отличники"
# reg = "Вася|Петя|Маша|Даша"
# print(re.findall(reg, s))

# a = "24-03-2026"
# reg =
# print(re.findall(reg, a))

# s = "int = 4, float = 4.0, double = 8.0f"
# # reg = r"\w+\s*=\s*\d[.\w+]*"
# # reg = r"int\s*=\s*\d[.\w+]*|float\s*=\s*\d[.\w+]*"
# reg = r"(?:int|float)\s*=\s*\d[.\w+]*"
# print(re.findall(reg, s))

# (?: ...) - обозначает что эти группирующие скобки являются не сохраняющими

# s = "127.0.0.1"
# # s = "192.255.255.255"
# # reg = r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}"
# reg = r"(?:\d{1,3}.){3}\d{1,3}"
# print(re.findall(reg, s))


# Рекурсия

# def elevator(n):
#     if n == 0:
#         print("Вы в подвале")
#         return
#     print("=>", n) # 5 4 3 2 1
#     elevator(n - 1)
#     print(n, end=" ")
#
#
# n1 = int(input("На каком вы этаже: "))
#
# elevator(n1)

# стек
# 1
# 2
# 3
# 4
# 5

# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res = res + i
#     return res
#
# print(sum_list([1,3,5,7,9]))


# def sum_list(lst):
#     if len(lst) == 1:
#         print(lst, "=>[0]: ", lst[0])
#         return lst[0]
#     else:
#         print(lst, "=>[0]: ", lst[0])
#         return lst[0] + sum_list(lst[1:])
#
# print(sum_list([1,3,5,7,9]))
#
# def to_str(n, base):
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n]
#     else:
#         return to_str(n // base, base) + convert[n % base]
# print(to_str(356,10))
# print(to_str(255,16)) #FF

# names = ["Adam",["Bob",["Chet","Cat"],"Bard","Bert"],"Alex",["Bea","Bill"],"Ann"]

# print(len(names))
# print(names[0])
# print(isinstance(names[0],list))
# print(names[1])
# print(isinstance(names[1],list))
# print(names[1][1])
# print(isinstance(names[1][1],list))
# print(names[1][1][0])
# print(isinstance(names[1][1][0],list))


# def func(item_list):
#     count = 0
#     for i in item_list:
#         if isinstance(i, list):
#             for j in i:
#                 if isinstance(j, list):
#                     for k in j:
#                         count += 1
#                 else:
#                     count += 1
#         else:
#             count += 1
#     return count
#
# print(func(names))

# names = ["Adam",["Bob",["Chet","Cat"],"Bard","Bert"],"Alex",["Bea","Bill"],"Ann"]
#
# def count_items(item_list):
#     count = 0
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_items(item)
#         else:
#             count += 1
#     return count
#
# print(count_items(names))


# def remove(text):
#     if not text:
#         return ""
#     if text[0] == '\t' or text[0] == " ":
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])
#
# print(remove(" Hello\tWorld "))

# f = open('text.txt', "r")

# print(f)
# print(*f)
#
# f.close()

# f = open(r'C:\Users\teacher\python54\test.txt', 'r')
#
# print(f)
# print(*f)
#
# f.close()

# print(f.closed)
# print(f.mode)
# print(f.name)
# print(f.encoding)

# print(f.read())
# print(f.read(3))

# print(f.readline())
# print(f.readline(3))
# print(f.readline())
# print(f.readline())

# f = open(r"text.txt")
# try:
#     print(f.read())
# finally:
#     f.close()

# print(f.readlines())
# print(f.readlines(5))

# for line in f:
#     print(line)

# f = open(r"text.txt")
# print(len(f.readlines()))

# cnt = 0
# for lene in f:
#     cnt += 1

# cnt = 0
# s = f.readline()
# while s !='':
#     s = f.readline()
#     cnt +=1
#
# print(cnt)

# f = open(r"text.txt", 'w')
# f.write("Python!")
# f.write("\nNew text")
# f.close()

# f = open("xyz.txt", 'a')
#
# # f.write("Hello World!")
# # f.write("\nNew text")
# # print(f.write("\nPYTHON"))
# lines = ["This is line 1","This is line 2","This is line 3"]
# f.writelines(lines)
# f.close()

# f = open("xyz.txt", 'w')
# lst = [str(i) + str(i-1) for i in range(1,20)]
# print(lst)
# for index in lst:
#     f.write(index + '\t')
# f.close()


# my_file = open("text2.txt", 'w')
# my_file.write('Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;')
# my_file.close()

# my_file = open("text2.txt", 'r')
# read_file = my_file.readlines()
# print(read_file)
# for i in range(len(read_file)):
#     if read_file[i] == "изменить строку в списке;\n":
#         read_file[i] = "Hello World\n"
# print(read_file)
# my_file.close()
# print(read_file)
#
# my_file = open("text2.txt", 'w')
# my_file.writelines(read_file)
# my_file.close()

# my_file = open("text3.txt", 'w')
# my_file.write('Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;')
# my_file.close()
#
# my_file = open("text3.txt", 'r')
# read_file = my_file.readlines()
# print(read_file)
# pos = int(input("Введите индес строки: "))
# if 0 <= pos <= len(read_file):
#     del  read_file[pos]
# else:
#     print("Неверный индекс")
#
# print(read_file)
# my_file.close()
# print(read_file)
#
# my_file = open("text3.txt", 'w')
# my_file.writelines(read_file)
# my_file.close()

# f = open("text.txt", 'r')
# print(f.read(3))
# print(f.tell()) # Возвращает позицию курсора
# print(f.seek(1)) # Перемещает курсор на позицию
# print(f.read())
# print(f.tell())
# f.close()


# f = open("text.txt", 'r+')
# print(f.write("I am learning Python!"))
# print(f.seek(3))
# print(f.write("-new string-"))
# print(f.tell())
# print(f.write("=PYTHON="))
# print(f.tell())
# f.close()


# with open("text.txt", 'w+') as f:
#     print(f.write("0123456789"))
#
# with open("text.txt", 'r') as f:
#     for line in f:
#         print(line[:6])
#
# file_name = "res.txt"
# lst = [2.8, 5.4, 6.7, 1.9, 7.999, 58.8445]
#
# def get_line(lt):
#     lt = list(map(str, lt))
#     # return lt
#     return " ".join(lt)
#
# # print(get_line(lst))
#
# with open(file_name, "w") as f:
#     f.write(get_line(lst))
#
# print("OK")

# file_name = "res.txt"
#
# with open(file_name, "r") as f:
#     nums = f.read()
#
# print(nums)
# num_list = list(map(float, nums.split()))
# print(num_list)
# print(len(num_list))


# with open("test.txt", "r") as f:
#     w = f.read().split()
#     print(w)
#     max_length = len(max(w, key=len))
#     print(max_length)
#     res = [word for word in w if len(word) == max_length]
#     print(res)

# text ="Cтрока №1\nCтрока №2\nCтрока №3\nCтрока №4\nCтрока №5\nCтрока №6\nCтрока №7\nCтрока №8\nCтрока №9\nCтрока №0\n"
#
# with open('one.txt', 'w') as f:
#     f.write(text)
#
# read_file = 'one.txt'
# write_file = 'two.txt'
#
# with open(read_file, 'r') as fr,open(write_file, 'w') as fw:
#     for line in fr:
#         line = line.replace("Cтрока", "Линия -> ")
#         fw.write(line)
#
# with open(write_file, "r") as fw:
#     for line in fw:
#         print(line,end='')

# f = open("test.txt")
# line = 0
#
# for i in f:
#     line +=1
#     word = 0
#     flag = 0
#
#     for j in i:
#         if j !=" " and flag == 0:
#             word +=1
#             flag = 1
#
#         elif j == " ":
#             flag = 0
#
#
#
#     print(i, len(i), "симв.", word, "сл.")
#
# print(line, "строки")
#
# f.close()

# Модули os и os.path

import os
import os.path


# print("Текущая директория: ", os.getcwd())
# print(os.listdir()) # Возвращает список файлов и папок, находяшихся в текушей директории(по умолчанию) или
# в директории по указанному пути
# print(os.listdir(r"..\..\..\..\.."))

# os.mkdir("folder") #создает директорию по указанному пути

# os.makedirs("nested1/nested2/nested3") #создает вложенные папки
# os.makedirs("nested1/nested2/nested4")

# os.remove("xyz.txt") # Удаляет файл(в обход корзины и безвозвратно)

# os.rename('nested1', "test") # Переименование папки или файла
# os.rename('text.txt', "text/text1.txt")

# os.rmdir("text")

# for root, dirs, files in os.walk("test", topdown=False):
#     print("Root: ", root)
#     print("\tSubdirs: ", dirs)
#     print("\t\tFiles: ", files)

# os.makedirs("Work/F1/f3")
# os.makedirs("Work/F2/f3")
# os.makedirs("Work/F3")

# def remove_empty_dirs(root_tres):
#     for root, dirs, files in os.walk(root_tres):
#         if not os.listdir(root):
#             os.rmdir(root)
#             print(f"Директория {root} удалена.")
#
# remove_empty_dirs("Work")

# def delete_folder(folder_path):
#     if not os.path.exists(folder_path):
#         print(f"Папка ={folder_path}= не существует")
#         return False
#
#     if not  os.path.isdir(folder_path):
#         print(f"={folder_path}= не папка")
#         return False
#
#     for root, dirs, files in os.walk(folder_path,topdown=False):
#         for file in files:
#             print(f"Удалено {file} файл")
#             file_path = os.path.join(root,file)
#             os.remove(file_path)
#
#         for dirr in dirs:
#             print(f"Удалено {dirr} папка")
#             dir_path = os.path.join(root, dirr)
#             os.rmdir(dir_path)
#
#     os.rmdir(folder_path)
#     print(f"Папка {folder_path} успешно удалена")
#     return True
#
# delete_folder("Base")

# print(os.path.split(r"C:\Users\teacher\python54\TopPython54\res.txt"))
# print(os.path.split(r"C:\Users\teacher\python54\TopPython54\\"))
#
# print(os.path.dirname(r"C:\Users\teacher\python54\TopPython54\res.txt"))
# print(os.path.basename(r"C:\Users\teacher\python54\TopPython54\res.txt"))

# print(os.path.join("C:\\Users", "teacher", "python54", "TopPython54", "res.txt"))

# print(os.path.exists(r"one1.txt"))
# print(os.path.exists(r"C:\Users\teacher\python54\TopPython54\test\nested2\nested3\text1.txt"))

# file = "one.txt"
#
# print(os.path.getatime(file))
# print(os.path.getmtime(file))
# print(os.path.getctime(file))
# print(os.path.getsize(file))

# import time
#
# path =r"C:\Program Files\JetBrains\PyCharm Community Edition 2024.2.2\plugins\python-ce\helpers\virtualenv-20.13.0.pyz"
#
# size = os.path.getsize(path)
# k_size = size // 1024
#
# print(f"Размер {k_size} kb")
#
# c_time = os.path.getctime(path)
# print(c_time)
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(c_time)))

# print(os.path.isfile(r"C:\Program Files\JetBrains\PyCharm Community Edition 2024.2.2\plugins\python-ce\helpers\virtualenv-20.13.0.pyz"))
# print(os.path.isdir(r"C:\Program Files\JetBrains\PyCharm Community Edition 2024.2.2\plugins\python-ce\helpers"))


# ООП - объектно ориентированно программирование

# свойства == переменные
# методы == функции
#
# атрибуты == свойства + методы

# class Point:
#     """Класс для представления координат на плоскости"""
#     x = 1
#     y = 1
#
#
# # print(Point.__doc__)
# # print(Point.__name__)
# # print(dir(Point))
#
# p1 = Point()
# # print(type(p1))
# # print(p1.x, p1.y)
# Point.x = 100
# p1.x = 200
# p1.y = 5
# # print(p1.x, p1.y)
# # print("ID POINT",id(Point))
# # print("ID p1",id(p1))
# print(p1.__dict__)
#
#
# p2 = Point()
# # print(p2.x, p2.y)
# print(p2.__dict__)
# print(Point.__dict__)
# # print("ID p2",id(p2))

# class Point:
#     """Класс для представления координат на плоскости"""
#     x = 1
#     y = 1
#
#     def set_cords(self):
#         # print(self.__dict__)
#         print("Hello World")
#
#
# p1 = Point()
# p1.x = 200
# p1.y = 5
# p1.set_cords()
# Point.set_cords(p1)
#
# p2 = Point()
# p2.set_cords()
# print(p2.x,p2.y)


# class Point:
#     x = 1
#     y = 1
#
#     def set_cords(self, x ,y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point()
# p1.set_cords(5, 10)
# print(p1.__dict__)
#
# p2 = Point()
# p2.set_cords(3, 6)
# print(p2.__dict__)
#
# Point.set_cords(p2,2,7)
# print(p2.__dict__)


# class Human:
#     name = "name"
#     birthday = "00.00.0000"
#     phohe = "00-00-00"
#     coutry = "coutry"
#     city = "city"
#     address = "street, house"
#
#     def input_info(self, name, birthday, phohe, coutry, city, address):
#         self.name = name
#         self.birthday = birthday
#         self.phohe = phohe
#         self.coutry = coutry
#         self.city = city
#         self.address = address
#
#     def print_info(self):
#         print("Персональные данные".center(40, "*"))
#         print(f"Имя {self.name} \nДата рождения {self.birthday}\n"
#               f"Номер телефона {self.phohe} \nСтрана {self.coutry}\n"
#               f"Город {self.city} \nДомашний алрес {self.address}"
#               )
#         print("*" * 40)
#
#     def set_name(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#     def set_birthday(self, birthday):
#         self.birthday = birthday
#
#     def get_birthday(self):
#         return self.birthday
#
#
# h1 = Human()
# h1.input_info("Юля", "25.05.1986", "45-56-67", "Россия", "СПБ", "Невский проспект, 122")
# h1.print_info()
# h1.set_name("Петр")
# print(h1.get_name())
# h1.set_birthday("19.12.1990")
# print(h1.get_birthday())
# print(h1.__dict__)


# class Point:
#     x = 1
#     y = 1
#
#
# p1 = Point()
# p1.x = 5
# p1.y = 10
# print(p1.__dict__)
# print(p1.x)
# # print(getattr(p1, "x"))
# # # print(p1.z)
# # print(getattr(p1, "z", "Нет атрибута"))
# # print(hasattr(p1, "z"))
# # p1.z = 7
# setattr(p1, "z", 7)
# # setattr(Point, "z", 7)
# delattr(p1, "z")
# print(p1.__dict__)


# class Person:
#     skill = 10
#     name = ""
#     surname = ""
#
#     def prin_info(self,name, surname):
#         print("Данные сотрудника",self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print("Квалификация сотрудника", self.skill,"\n")
#
#
# p1 = Person()
# p1.prin_info("Viktor", "Reznik")
# p1.add_skill(3)
#
# p2 = Person()
# p2.prin_info("Anna", "Dolgih")
# p2.add_skill(2)

# Специальные методы
# - конструктор (__new__)
# - инструктор (__init__)
# - деструктор (__del__)


# class Point:
#     # def __new__(cls, *args, **kwargs):
#     #     print("this is constructor")
#     #     return super().__new__(cls)
#
#     def __init__(self):
#         print("this is initializator")
#
#
# p1 = Point()


# class Person:
#     skill = 10
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname= surname
#
#     def prin_info(self):
#         print("Данные сотрудника",self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print("Квалификация сотрудника", self.skill,"\n")
#
#
# p1 = Person("Viktor", "Reznik")
# p1.prin_info()
# p1.add_skill(3)
#
# p2 = Person("Anna", "Dolgih")
# p2.prin_info()
# p2.add_skill(2)

# class Point:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __del__(self):
#         print("Удаление экземпляра " + self.__class__.__name__)
#
#
# p1 = Point(5, 10)
# print(p1.__dict__)
# p1 = 0
# del  p1
# print(p1.__dict__)
# print(p1.x)

# class Point:
#     count = 0 # Статическое свойство
#
#
#     def __init__(self, x=0, y=0): # Динамические свойства
#         self.x = x
#         self.y = y
#         # self.count += 1
#         Point.count += 1
#
#
#
#
# p1 = Point(5, 10)
# print(p1.count)
# p2 = Point(15, 20)
# p3 = Point(25, 30)
#
# print(Point.count)
# print(p1.count)

# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print("Инициализация робота", self.name)
#         Robot.k +=1
#
#     def say_hi(self):
#         print("Привет! Меня зовут ", self.name)
#
#     def __del__(self):
#         print(self.name, "выключается")
#         Robot.k -= 1
#         if Robot.k == 0:
#             print(self.name, "был поледний робот")
#         else:
#             print("Работающих роботов", Robot.k)
#
#
# r1 = Robot("R2-D2")
# r1.say_hi()
# print("Численность роботов", Robot.k)
#
# r2 = Robot("C-3PO")
# r2.say_hi()
# print("Численность роботов", Robot.k)
#
# r3 = Robot("Е-8WO")
# r3.say_hi()
# print("Численность роботов", Robot.k)
#
# print()
# print("Роботы закончили работу")
# del r1
# del r2
# del r3
# print("Численность роботов", Robot.k)

# Инкапсуляция - способность скрывать свойства от пользователя для защиты от изменений
# public (self.x) публичные свойства
# protected (self._x) используются при наследовании
# private (self.__x) Защищенные свойства

# class Point:
#     def __init__(self, x, y):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def __check_value(q):
#         if isinstance(q, int) or isinstance(q, float):
#             return True
#         return False
#
#     def set_coords(self, x, y):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_coords(self):
#         return self.__x, self.__y
#
#     def set_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Координаты должны быть числами")
#
#     def set_y(self, y):
#         if Point.__check_value(y):
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_x(self):
#         return self.__x
#
#     def get_y(self):
#         return self.__y
#
#
# p1 = Point(5, 10)
# print(p1.__dict__)
# p1.set_coords(1, 2)
# # p1.__x = 100
# # p1.__y = 100
# p1.set_x(4)
# print(p1.get_coords())
# print(p1.__dict__)
# print(p1.get_x())
# # print(p1.__x, p1.__y)


# class Car:
#     def __init__(self, name, year, model, power, color, price):
#         self.__name = self.__model = self.__color = "Некорректные данные"
#         self.__year = self.__power = self.__price = 0
#
#         if Car.__check_value_str(name):
#             self.__name = name
#         if Car.__check_value_int(year):
#             self.__year = year
#         if Car.__check_value_str(model):
#             self.__model = model
#         if Car.__check_value_int(power):
#             self.__power = power
#         if Car.__check_value_str(color):
#             self.__color = color
#         if Car.__check_value_int(power):
#             self.__price = price
#
#     def set_name(self,name):
#         if Car.__check_value_str(name):
#             self.__name = name
#
#     def get_name(self):
#         return self.__name
#
#     def print_info(self):
#         print(f"Название {self.__name}")
#         print(f"Год выпуска {self.__year}")
#         print(f"Производитель {self.__model}")
#         print(f"Мощность двигателя {self.__power}")
#         print(f"Цвет машины {self.__color}")
#         print(f"Цена {self.__price}")
#
#     def __check_value_str(s):
#         if not isinstance(s, str):
#             print("Данные должны быть строкой")
#             return False
#         return True
#
#     def __check_value_int(s):
#         if not isinstance(s, int):
#             print("Данные должны быть числом")
#             return False
#         return True
#
#
# c1 = Car("X7 M50i", "2021", "BMW", 530, "white", 10790000)
# c1.print_info()
# c1.set_name("X5")
# print("=" * 40)
# print(c1.get_name())

# class Point:
#     # __slots__ = ['__x','__y'] # устнавливает ограничения на свойства
#
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __set_x(self, x):
#         print("__set_x")
#         self.__x = x
#
#     def __get_x(self):
#         print("__get_x")
#         return self.__x
#
#     def __del_x(self):
#         print("__del_x")
#         del self.__x
#
#     cord_x = property(__get_x, __set_x, __del_x)
#
# p1 = Point(5, 10)
# print(p1.__dict__)
#
# print("=" * 35)
#
# p1.cord_x = 100
# print(p1.cord_x)
# del p1.cord_x
# p1.cord_x = 33
# print(p1.__dict__)

# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     @property
#     def cord_x(self): #__get_x
#         print("__get_x")
#         return self.__x
#
#     @cord_x.setter
#     def cord_x(self, x): #__set_x
#         print("__set_x")
#         self.__x = x
#
#     @cord_x.deleter
#     def cord_x(self): # __del_x
#         print("__del_x")
#         del self.__x
#
#     # cord_x = property(__get_x, __set_x, __del_x)
#
# p1 = Point(5, 10)
# print(p1.__dict__)
#
# print("=" * 35)
#
# p1.cord_x = 35
# print(p1.cord_x)
# del p1.cord_x
# p1.cord_x = 88
# print(p1.__dict__)
#
#
# class Person:
#     def __init__(self, name, old):
#         self.__name = name
#         self.__old = old
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         self.__name = name
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self,old):
#         self.__old = old
#
#     @old.deleter
#     def old(self):
#         del self.__old
#
# p1 = Person("Irina", 26)
# print(p1.name)
# p1.name = "igor"
# p1.old = 30
# del p1.name
# del p1.old
#
# p1.name = "Ivan"
# p1.old = 55
# print(p1.__dict__)


# class Point:
#     __count = 0 # Статическое свойство
#
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#         Point.__count += 1
#
#     @staticmethod
#     def get_count():
#         return Point.__count
#
#
# p1 = Point()
# print("p1 = ", p1.get_count())
# p2= Point()
# print("p2 = ", Point.get_count())
# p3 = Point()
# print("p3 = ", p1.get_count())

# class Point:
#     __count = 0 # Статическое свойство
#
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#         Point.__count += 1
#
#     @staticmethod
#     def get_count():
#         return Point.__count
#
#
# p1 = Point()
# print("p1 = ", Point.get_count())
# p2= Point()
# print("p2 = ", Point.get_count())
# p3 = Point()
# print("p3 = ", p1.get_count())

# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
# print(Change.inc(10), Change.dec(10))

#
# class Date:
#     def __init__(self, day=0, month=0, year=0):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     def string_to_db(self):
#         return f"{self.day}-{self.month}-{self.year}"
#
#     @classmethod
#     def from_string(cls, data_as_string):
#         d, m, y = map(int, data_as_string.split("."))
#         return cls(d, m, y)
#
#     @staticmethod
#     def is_data_valid(data_as_string):
#         if data_as_string.count(".") == 2:
#             d, m, y = map(int, data_as_string.split("."))
#             return d <= 31 and m <= 12 and y <= 2500
#
# dates = [
#     "16.04.2025",
#     "16-04-2025",
#     "04.16.2025",
#     "26.04.2025"
# ]
#
# for string_data in dates:
#     if Date.is_data_valid(string_data):
#         data = Date.from_string(string_data)
#         string_to_db = data.string_to_db()
#         print(string_to_db)
#     else:
#         print("Некорректная дата")

# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = "RUB"
#     suffix_usd = "USD"
#     suffix_eur = "EUR"
#
#     def __init__(self, num, surname, percent, value=0):
#         self.__num = num
#         self.surname = surname
#         self.percent = percent
#         self.value = value
#         print(f"Счет #{self.num} принадлежащий {self.surname} был открыт.")
#         print("*" * 40)
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.value} {Account.suffix}")
#
#     def prin_info(self):
#         print(f"Информация о счете")
#         print('-' * 30)
#         print(f"# {self.num}")
#         print(f"Владелец: {self.surname}")
#         self.print_balance()
#         print(f"Проценты: {self.percent:.0%}")
#         print('-' * 30)
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f'Состояние счета: {usd_val} {Account.suffix_usd}')
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.value, Account.rate_eur)
#         print(f'Состояние счета: {eur_val} {Account.suffix_eur}')
#
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def add_percents(self):
#         self.value += self.percent * self.value
#         print(f"Проценты были успешно выплачены")
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f"К сожалению у вас нет {val} {Account.suffix}")
#         else:
#             self.value -= val
#             print(f"{val} {Account.suffix} было успешно снято!")
#         self.print_balance()
#     def add_money(self, val):
#         self.value += val
#         print(f"{val} {Account.suffix} было успешно добавленно!")
#         self.print_balance()
#
#     def __del__(self):
#         print("*" * 50)
#         print(f"Счет #{self.num} принадлежащий {self.surname} был закрыт.")
#
# acc = Account("123456", "Долгих", 0.03, 1000)
# acc.prin_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# Account.set_usd_rate(2)
# acc.convert_to_usd()
# Account.set_eur_rate(3)
# acc.convert_to_eur()
#
# acc.edit_owner("Дюма")
# acc.prin_info()
#
# print()
# acc.add_percents()
# print()
# acc.withdraw_money(5000)
# acc.withdraw_money(1000)
# print()
# acc.add_money(5000)
# import re
#
#
# class UserData:
#     def __init__(self, fio, old, ps, weight):
#         # self.verify_fio(fio)
#         # self.verify_old(old)
#         # self.verify_ps(ps)
#         # self.verify_weight(weight)
#         #
#         # # self.__fio = fio
#         # self.__old = old
#         # self.__ps = ps
#         # self.__weight = weight
#
#         self.fio = fio
#         self.old = old
#         self.ps = ps
#         self.weight = weight
#
#     @classmethod
#     def verify_fio(cls, fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО должно быть строкой")
#         f = fio.split()
#         if len(f) != 3:
#             raise TypeError("Неверный формат ФИО")
#         letters = "".join(re.findall(r"[a-zа-яё-]", fio, flags=re.IGNORECASE))
#         for s in f:
#             if len(s.strip(letters)) != 0:
#                 raise TypeError("В ФИО можно использовать только буквы и дефис")
#
#     @classmethod
#     def verify_old(cls, old):
#         if not isinstance(old, int) or old < 18 or old > 100:
#             raise TypeError("Возраст должен быть числом в диапазоне от 18 до 100")
#
#     @classmethod
#     def verify_ps(cls, ps):
#         if not isinstance(ps, str):
#             raise TypeError("Паспорт должен быть строкой")
#         s = ps.split()
#         # print(s)
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError("Неверный формат паспорта")
#         for p in s:
#             if not p.isdigit():
#                 raise TypeError("Серия и номер должны быть числами")
#
#     @classmethod
#     def verify_weight(cls, w):
#         if not isinstance(w, float) or w < 50:
#             raise TypeError("Вес должен быть вешественным число от 50 кг")
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
#     def old(self, old):
#         self.verify_old(old)
#         self.__old = old
#
#     @property
#     def ps(self):
#         return self.__ps
#
#     @ps.setter
#     def ps(self, ps):
#         self.verify_ps(ps)
#         self.__ps = ps
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
#
# p1 = UserData("Иванов Иван Иванович", 26, "1234 567890", 80.1)
# print(p1.__dict__)
# p1.fio =  "Петров Петр Петрович"
# print(p1.fio)
# p1.old = 30
# p1.ps = "4321 987654"
# p1.weight = 70.0
#
# print(p1.__dict__)

# class Point(object):
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "green", width: int =1):
#         print("Инициализатор Prop")
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
#         print("Инициализатор класса Line")
#         # Prop.__init__(self, *args)
#         super().__init__(*args)
#         self.__width = 5
#
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self.__width}, {self.get_width()}")
#
#
# class Rect(Prop):
#     def __init__(self, sp, ep, color = "green", width =1, bg="yellow"):
#         super().__init__(sp, ep, color, width)
#         self.background = bg
#
#     def draw_rect(self):
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self.get_width()}, {self.background}")
#
# line = Line(Point(1, 2), Point(10, 20), "red", 2)
# line.draw_line()
#
# rect = Rect(Point(30, 40), Point(70, 80))
# rect.draw_rect()
# print(line.__dict__)
# # print(issubclass(Point, object))


# class Figure:
#     def __init__(self, color):
#         self.__color = color
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
#         self.__width = width
#         self.__height = height
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
#             raise ValueError
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
#             raise ValueError
#
#     def area(self):
#         print(f"Площадь {self.color} прямоугольника:")
#         # return self.__width * self.__height
#         return self.width * self.height
#
#
# rect = Rectangle(10,20,"green")
# # print(rect._width)
# rect.width = 5
# print(rect.width)
# print(rect.height)
# print(rect.color)
# rect.color = "Красный"
# print(rect.color)
# print(rect.area())


# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_digit(self):
#         if not isinstance(self.__x, (int, float)) or not isinstance(self.__y, (int, float)):
#             print("Координаты должны быть чимлом")
#             return False
#         return True
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "green", width: int =1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coords(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#
#
# class Line(Prop):
#
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# # class Rect(Prop):
# #     def __init__(self, sp, ep, color = "green", width =1, bg="yellow"):
# #         super().__init__(sp, ep, color, width)
# #         self.background = bg
# #
# #     def draw_rect(self):
# #         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self.get_width()}, {self.background}")
#
# line = Line(Point("1",2), Point(10,20))
# line.draw_line()
# line.set_coords(Point("5",25), Point(15,30))
# line.draw_line()

# class Rect:
#     def __init__(self, w, h):
#         self.width = w
#         self.height = h
#
#     def show_rect(self):
#         print(f"Прямоугольник:\nШирина {self.width} \nВысота {self.height}")
#
#
# class RectFon(Rect):
#     def __init__(self, w, h, bg):
#         super().__init__(w,h)
#         self.fon = bg
#
#     def show_rect(self):
#         super().show_rect()
#         print(f"Рамка {self.fon}")
#
#
# class RectBorder(Rect):
#     def __init__(self, w, h, b):
#         super().__init__(w,h)
#         self.border = b
#
#     def show_rect(self):
#         super().show_rect()
#         print(f"Граница {self.border}")
#
#
#
#
# r1 = RectFon(400,200, "green")
# r1.show_rect()
#
# r2 = RectBorder(600,300, "1px solid red")
# r2.show_rect()

# class Vector(list):
#     def __str__(self):
#         return ' '.join(map(str, self))
#
#
# v = Vector([1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(v)
# print(type(v))
#
# q = Vector((1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(q)

# Перегрузка методов

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_digit(self):
#         if not isinstance(self.__x, (int, float)) or not isinstance(self.__y, (int, float)):
#             print("Координаты должны быть числом")
#             return False
#         return True
#
#     def is_int(self):
#         if not isinstance(self.__x, int) or not isinstance(self.__y, int):
#             print("Координаты должны быть целочисленным")
#             return False
#         return True
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "green", width: int =1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coords(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#
#
# class Line(Prop):
#
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#     def set_coords(self, sp, ep=None):
#         if ep is None:
#             if sp.is_int():
#                 self._sp = sp
#         else:
#             if sp.is_int() and ep.is_int():
#                 self._sp = sp
#                 self._ep = ep
#
#
#
# line = Line(Point("1",2), Point(10,20))
# line.draw_line()
# # line.set_coords(Point(5,25), Point(15,30))
# # line.draw_line()
#
# line.set_coords(Point(-5,-25))
# line.draw_line()

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_digit(self):
#         if not isinstance(self.__x, (int, float)) or not isinstance(self.__y, (int, float)):
#             print("Координаты должны быть числом")
#             return False
#         return True
#
#     def is_int(self):
#         if not isinstance(self.__x, int) or not isinstance(self.__y, int):
#             print("Координаты должны быть целочисленным")
#             return False
#         return True
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "green", width: int =1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coords(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#
#     def draw(self): #Абстрактный метод
#         raise  NotImplementedError("В дочернем классе должен быть определн мотод draw()")
#
# class Line(Prop):
#
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
# class Rect(Prop):
#     pass
#     # def draw(self):
#     #     print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
# class Ellips(Prop):
#     def draw(self):
#         print(f"Рисование элипса: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# firgs = list()
# firgs.append(Line(Point(8,8), Point(10,10)))
# firgs.append(Line(Point(80,80), Point(100,1000)))
# firgs.append(Rect(Point(8,8), Point(10,10)))
# firgs.append(Ellips(Point(8,8), Point(10,10)))
#
# for f in firgs:
#     f.draw()

# import math
#
# class Table:
#     def __init__(self, width=None, length=None,radius=None ):
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
#         raise NotImplementedError("В дочернем классе должен быть метод calc_area()")
#
# class SqTable(Table):
#     def calc_area(self):
#         return self._width * self._length
#
# class RoundTable(Table):
#     def calc_area(self):
#         return round(math.pi * self._radius ** 2, 2)
#
# t = SqTable(20,10)
# print(t.__dict__)
# print(t.calc_area())
#
# t1 = SqTable(20)
# print(t1.__dict__)
# print(t1.calc_area())
#
# t2 = RoundTable(radius=20)
# print(t2.__dict__)
# print(t2.calc_area())

# from abc import ABC, abstractmethod
#
# class Chess(ABC):
#     def draw(self):
#         print("Нарисовал шахматную фигуру")
#
#     @abstractmethod
#     def move(self):
#         # pass
#         print("Вызов методы move()")
#
# class Horse(Chess):
#     pass
#     # def move(self):
#     #     super().move()
#     #     print("Конь походил e2e4")
#
#
# # q = Chess()
# q = Horse()
# q.draw()
# q.move()

from abc import ABC, abstractmethod

class Currency(ABC):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def convert_to_rub(self):
        pass

    def print_value(self):
        print(self.value, end=' ')

class Dollar(Currency):
    rate_to_rub = 75.18
    suffix = "USD"

    def convert_to_rub(self):
        rub = self.value * Dollar.rate_to_rub
        return rub

    def print_value(self):
        super().print_value()
        print(Dollar.suffix, end=" ")

class Euro(Currency):
    rate_to_rub = 95.18
    suffix = "EUR"

    def convert_to_rub(self):
        rub = self.value * Euro.rate_to_rub
        return rub

    def print_value(self):
        super().print_value()
        print(Euro.suffix, end=" ")


d = [Dollar(5),Dollar(10),Dollar(50),Dollar(100)]
e = [Euro(5),Euro(10),Euro(50),Euro(100)]

print("*" * 30)
for i in d:
    i.print_value()
    print(f"= {i.convert_to_rub():.2f} RUB")

print("*" * 30)
for i in e:
    i.print_value()
    print(f"= {i.convert_to_rub():.2f} RUB")