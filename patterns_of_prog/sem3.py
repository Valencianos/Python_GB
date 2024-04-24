map = [1, 2, 3,
        4, 5, 6,
        7, 8, 9]

wins = [[0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]]

def print_map():
    print(map[0], end=" ")
    print(map[1], end=" ")
    print(map[2])

    print(map[3], end=" ")
    print(map[4], end=" ")
    print(map[5])

    print(map[6], end=" ")
    print(map[7], end=" ")
    print(map[8])


def step_maps(step, symbol):
    ind = map.index(step)
    map[ind] = symbol

def get_result():
    win = ""

    for i in wins:
        if map[i[0]] == "X" and map[i[1]] == "X" and map[i[2]] == "X":
            win = "X"
        if map[i[0]] == "O" and map[i[1]] == "O" and map[i[2]] == "O":
            win = "O"
    return win

game_over = False
player1 = True

while game_over == False:
    print_map()
    if player1 == True:
        symbol = "X"
        step = int(input("Player 1, your turn: "))
    else:
        symbol = "O"
        step = int(input("Player 2, your turn: "))

    step_maps(step, symbol)
    win = get_result()
    if win != "":
        game_over = True
    else:
        game_over = False
    player1 = not (player1)

print_map()
print("And the winner is: ", win)