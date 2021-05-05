cells = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]


def print_match():
    print("---------")
    print("| " + cells[0][0] + " " + cells[0][1] + " " + cells[0][2] + " |")
    print("| " + cells[1][0] + " " + cells[1][1] + " " + cells[1][2] + " |")
    print("| " + cells[2][0] + " " + cells[2][1] + " " + cells[2][2] + " |")
    print("---------")


def enter_coordinates(symbol):
    global cells
    coordinates = input("Enter the coordinates: ").split()

    if coordinates[0] not in "0123456789" or coordinates[1] not in "0123456789":
        print("You should enter numbers!")
        enter_coordinates(symbol)
        return False

    x = int(coordinates[0])
    y = int(coordinates[1])

    if x < 1 or x > 3 or y < 1 or y > 3:
        print("Coordinates should be from 1 to 3!")
        enter_coordinates(symbol)
        return False

    x = x - 1
    y = y - 1

    if cells[x][y] != " ":
        print("This cell is occupied! Choose another one!")
        enter_coordinates(symbol)
        return False
    else:
        cells[x][y] = symbol
        return True


def check_win(symbol):
    for x in range(3):
        if cells[x][0] == symbol and cells[x][1] == symbol and cells[x][2] == symbol:
            return True
    for x in range(3):
        if cells[0][x] == symbol and cells[1][x] == symbol and cells[2][x] == symbol:
            return True
    if cells[0][0] == symbol and cells[1][1] == symbol and cells[2][2] == symbol:
        return True
    elif cells[0][2] == symbol and cells[1][1] == symbol and cells[2][0] == symbol:
        return True
    else:
        return False


print_match()
current_symbol = "X"

while True:
    enter_coordinates(current_symbol)
    print_match()

    x_wins = check_win('X')
    o_wins = check_win('O')

    x_count = len([x for x in cells if x == 'X'])
    o_count = len([x for x in cells if x == 'O'])

    if x_wins and not o_wins:
        print("X wins")
        break
    elif o_wins and not x_wins:
        print("O wins")
        break
    elif cells[0].count(" ") + cells[1].count(" ") + cells[2].count(" ") == 0:
        print("Draw")
        break

    if current_symbol == "X":
        current_symbol = "O"
    else:
        current_symbol = "X"
