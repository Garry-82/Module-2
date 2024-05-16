print("---Добро пожаловать в Крестики-Нолики---")
print("----------------------------------------")
game_land = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]  #  -  переменная игрового поля
def print_game_lend(list_):  #  - функция распечатки игрового поля с указанными значениями
    print("   ",*list_[0])
    print("   ",*list_[1])
    print("   ",*list_[2])
print_game_lend(game_land)
def chek_win(list_):  #  -  функция проверки победителя
    if list_[0] == ["X", "X", "X"] or list_[1] == ["X", "X", "X"] or list_[2] == ["X", "X", "X"] or list_[0][0] == \
            list_[1][0] == list_[2][0] == "X" or list_[0][1] == list_[1][1] == list_[2][1] == "X" or \
            list_[0][2] == list_[1][2] == list_[2][2] == "X" or list_[0][0] == list_[1][1] == list_[2][2] == "X" or \
            list_[0][2] == list_[1][1] == list_[2][0] == "X":
        print("Победа КРЕСТИКОВ!!!")
        return "win"
    if list_[0] == ["O", "O", "O"] or list_[1] == ["O", "O", "O"] or list_[2] == ["O", "O", "O"] or list_[0][0] == \
            list_[1][0] == list_[2][0] == "O" or list_[0][1] == list_[1][1] == list_[2][1] == "O" or \
            list_[0][2] == list_[1][2] == list_[2][2] == "O" or list_[0][0] == list_[1][1] == list_[2][2] == "O" or \
            list_[0][2] == list_[1][1] == list_[2][0] == "O":
        print("Победа НОЛИКОВ!!!")
        return "win"
a = ""
list_simbol = ["X", "O", "X", "O", "X", "O", "X", "O", "X"]
a = input("Приступим к игре! Если готов, нажми любую клавишу! __", )
if a != "":
    i = 0
    while i < len(list_simbol):
        print("сейчас ход:___", list_simbol[i], "___")
        num_str = input("Введите номер строки (1, 2 или 3): ", )
        while num_str != "1" and num_str != "2" and num_str != "3":
            num_str = input("Вы ввели некорректные данные!! Повторите ввод одного из чисел (1,2,3): ", )
        num_columb = input("Введите номер столбца (1, 2 или 3): ", )
        while num_columb != "1" and num_columb != "2" and num_columb != "3":
            num_columb = input("Вы ввели некорректные данные!! Повторите ввод одного из чисел (1,2,3): ", )
        if game_land[int(num_str) - 1][int(num_columb) - 1] == "*":
            game_land[int(num_str) - 1][int(num_columb) - 1] = list_simbol[i]
            print_game_lend(game_land)
            if chek_win(game_land) == "win":
                break
            else:
                i = i + 1
        else:
            print("Данное игровое поле уже занято! Повторите ввод..")
else:
    print("Чтож, сыграем в другой раз!! Пока...")
