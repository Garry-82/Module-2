def podbor_key(a):  #  функция вывода ключа ля заданного числа
    key = ""
    for i in range(1, a):
        for j in range(i + 1, a):
            sum_ = i + j
            if a % sum_ == 0:
                key = key + str(i) + str(j)
    return key

char=input('введите любое число "от 3 до 20 включительно": ',)
if char.isdigit() != True:
    print("Вы ввели не число! Будьте внимательнее!!!")
else:
    if int(char) < 3 or int(char) > 20:
        print("Вы ввели число не из требуемого диапазона! Будьте внимательны!!!")
    else:
        print(f"Код для введенного вами числа ",*{char}," будет: ",podbor_key(int(char)))
