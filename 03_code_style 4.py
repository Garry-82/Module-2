# -*- coding: utf-8 -*-

# блоки кода

x, y = 10, 29

if x < 0:
    print('Х меньше нуля')
    z = x ** 2 + y
else:
    print('Х больше нуля')
    z = x - y
print('Результат', z)

# ср. с С++

# if (x < 0) { printf('Меньше нуля\n'); z = x**2 + y; } else { printf('Больше нуля\n'); z = x - y; }
# printf('Получается\n', z)

# вложенные блоки кода

name = input('Enter your name: ')
if name == 'Ola':
    print('Hi, Ola!')
if name == 'Sofi':
    print('Hi, Sofi!')
if name == 'Katy':
    print('Hi, Katy!')
else:
    print('Hi, anonymous!')

# оператор pass

if x < 0:
    if y > 0:
        z = -x + y
    else:
        z = -x - y
else:
    z = x + y

# соглашения о стиле кода
# PEP8 (Python Enhancement Proposal 8) - описан "правильный" стиль программирования в пайтон
# https://www.python.org/dev/peps/pep-0008/

# 4 пробела на каждый уровень отступа

if x < 0:
    if y > 0:
        pass
    else:
        print('направо!')
else:
    print('стой!')

# Максимальная длина строки

my_poem = ['Варкалось. Хливкие шорьки'  # фрагмент поэмы Jabberwocky из «Алисы в Зазеркалье» Льюиса Карола в переводе
           'пырялись по наве',
           'И хрюкотали зелюки,'
           'Как мюмзики в мове.',
           'О бойся Бармаглота, сын!'
           'Он так свирлеп и дик',
           'А в глуще рымит исполин -'
           'Злопастный Брандашмыг']

# пробелы в операторах

x = 2
y = x * x + 1
is_big = x >= 3000

x = my_poem[-1]
print(x)
my_list = [2, 3, 4, 5, 6, ]

# reformat кода

x, y = 3, 8

if x == 3:
    print(42)

if x < 0:
    if y > 0:
        print('налево!')
    else:
        print('направо!')
else:
    print('стой!')

# названия переменных

number = 34
if number > 10:
    print('I need more space for my pets!')

favorite = ['cat', 'wolf', 'ostrich']  # favorite - список любимых животных
if 'lion' in favorite:
    print('Wow!')

# рекомендации PEP8

# b (одиночная маленькая буква)
# B (одиночная заглавная буква)
# но лучше использовать только такие одно буквенные имена
#   i j k - для циклов
#   x y z - для координат

# никогда не используйте в названиях переменных одиночные l, I, O !
b = 34
c = 43
if b > c:
    print("b>c")
else:
    print("b не больше c")
d = 9
if d > 0:
    print("d>0")

# lowercase (слово в нижнем регистре)
# lower_case_with_underscores (слова из маленьких букв с подчеркиваниями)
# UPPERCASE (заглавные буквы)
# UPPERCASE_WITH_UNDERSCORES (слова из заглавных букв с подчеркиваниями)

# CapitalizedWords (слова с заглавными буквами, или CapWords, или CamelCase).
#   Замечание: когда вы используете аббревиатуры в таком стиле, пишите все буквы аббревиатуры заглавными —
#   HTTPServerError лучше, чем HttpServerError.

# mixedCase (отличается от CapitalizedWords тем, что первое слово начинается с маленькой буквы)
# Capitalized_Words_With_Underscores (слова с заглавными буквами и подчеркиваниями — уродливо!)


# автоматическое переименование в PyCharm и подсказки - вам не нужно набирать длинные названия переменных

ss = ['cat', 'wolf', 'ostrich']  # ss - список любимых животных
if 'lion' in ss:
    print('Wow!')

# В каждой уважающей себя компании есть style guide (стайл-гайд) - руководство по стилю написания кода.
# Практически все они основываются на PEP8, с небольшими исключениями, принятыми в этой команде.
# Как пример стайл-гайда небольшой компании рекомендую почитать
# https://github.com/best-doctor/guides/blob/master/guides/python_styleguide.md