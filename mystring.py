s = input()  # вводит строчное значение с клавиатуры


print('4'*4)  # вывело 4444


# при умножении строки на целое число строка дублируется
name = input('введите своё имя: ')
result = f'пользователь ввёл имя {name}'  # через f строку можно добавлять любую переменную в строку
print(result)


# СРЕЗЫ СТРОК
x = '987654321'
print(x[2:5])  # вывело 765

print(x[:5])
print(x[2:])

print(x[::2])  # выводит каждое второе значение
print(x[::-1])  # выводит стоку в обратном порядке (аналог команды .reverse для списков)

# ОСНОВНЫЕ МЕТОДЫ СТРОК
y = '987654321'
y = y.replace('65', '*')  # заменняет подстроку на другую подстроку
print(y.count('*'))  # выводит кол-во передаваемых элементов строки
print(y.index('*'))  # выводит первый найденный индекс элемента
M = y.split('*')  # разбивает строку на список строк по определённому символу
print(M)
s = '**'.join(M)  # из списка строк возвращает целую строку
print(s)
print(s.upper())  # делает все буквы большими
print(s.lower())  # делает все буквы маленькими
print(s.strip())  # удаляет лишние пробелы слева и справа
