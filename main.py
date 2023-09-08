win_state = False
win_states = ((1, 2, 3), (4, 5, 6), (7, 8, 9),
              (1, 4, 7), (2, 5, 8), (3, 6, 9),
              (1, 5, 9), (3, 5, 7))
field = list(range(1, 10))
counter = 0
player = ""
while win_state is False:
    valid = False
    if counter % 2:
        player = "O"
    else:
        player = "X"
    counter += 1
    print(f"Система: Ход игрока {player}!")
    for index in range(1, 10, 3):
        print(field[index-1], field[index], field[index+1])
    while valid is False:
        position = int(input("Игрок "+player+": Клетка: "))
        if str(field[position-1]) in "OX":
            print("Система: Клетка уже занята!")
        else:
            field[position-1] = player
            valid = True
    if counter > 4:
        for state in win_states:
            if field[state[0]-1] ==  field[state[1]-1] ==  field[state[2]-1]:
                print(f"Система: {player} победил (-а)!")
                win_state = True
    if counter >= 9:
        print(f"Система: Ничья!")
        win_state = True
