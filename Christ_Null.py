def greet():
    print("-----------------------")
    print("Приветствуем в чертогах")
    print(" разума под названием  ")
    print("  крестики-нолики х_0  ")
    print("-----------------------")
    print(" наш формат ввода: x y ")
    print(" где x - номер строки  ")
    print(" а y - номер столбца   ")

def show_field():
    print()
    print(" К решению судьбы приготовиться 0_0")
    print()
    print("   | 0 | 1 | 2 |")
    print(" ---------------")
    for i, row in enumerate(field):
        row_str = f" {i} | {' | '.join(row)} | "
        print(row_str)
        print(" --------------- ")
    print()

def ask():
    while True:
        cords = input("  Вращайте барабан: ").split()

        if len(cords) != 2:
            print(" Подайте две координаты, уважаемый/ая! ")
            continue

        x, y = cords

        if not(x.isdigit()) or not(y.isdigit()):
            print(" Введите числа ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Простите, мимо кассы! ")
            continue

        if field[x][y] != " ":
            print(" Клеточка закрыта! ")
            continue

        return x, y

def check_win_combination():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print(" Победили крестоносцы, Deus Vult !")
            return True
        if symbols == ["0", "0", "0"]:
            print(" Победителей не судят 0_о !")
            return True
    return False


greet()
field = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    show_field()
    if count % 2 == 1:
        print(" Ходят крестоносцы !")
    else:
        print(" Ступает нолик!")

    x, y = ask()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win_combination():
        break

    if count == 9:
        print(" Главное - не победа, а участие!")
        break
