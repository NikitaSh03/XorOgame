#Крестики нолики
field = [["-"]*3 for _ in range(3)]
def show_field(field):
    print("---------------------------------------------")
    print("  0 1 2")
    for i in range(len(field)):
        print(str(i), *field[i])
    print("---------------------------------------------")



def x_or_o_print(f):
    while True:
        x, y = input("Введите координату по оси --x--  "), input("Введите координату по оси --y--  ")
        if x.isdigit() and y.isdigit:
            if 2>=int(y)>=0 and 2>=int(x)>=0:
                break
            else:
                print("Введённые числа должны быть в диапозоне 0 - 2! ")
                continue
        else:
            print("Введённые числа должны быть в диапозоне 0 - 2! ")
            continue
        if f[y][x] != "-":
            print("Тут уже что-то стоит) выберите другое поле !")
            continue
        else:
            break
    return x, y


def Startfunc(field):
    counter = 0
    while True:
        show_field(field)
        if counter < 9:
            if counter % 2 == 0:
                x, y = x_or_o_print(field)
                x, y = int(x), int(y)
                field[x][y] = 'x'
                user = 'x'
            else:
                x, y = x_or_o_print(field)
                x, y = int(x), int(y)
                field[x][y] = 'o'
                user = 'o'

        elif counter == 9:
            print('Ничья')
            break
        if check_winner(field,user):
            print(f"Выйграл {user}")
            break
        counter+=1

def check_winner(f, user):
    f_list = []

    for l in f:
        f_list += l

    positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    indices = set([i for i, x in enumerate(f_list) if x == user])

    for p in positions:
        if len(indices.intersection(set(p))) == 3:
            return True
    return False

Startfunc(field)
