import random as rd


def the_game():
    trial = 1000 # run the simulation 1000 times
    k_win, s_win = 0, 0
    for _ in range(trial):
        doors = [1, 2, 3] # a list with 3 doors
        win = rd.choice(doors)

        choice = rd.choice(doors)

        if win == choice: # adding 1 random door is equivalent to removing 1 random door
            after_choose = [win]
            after_choose.append(rd.choice([d for d in doors if d not in after_choose]))
        elif win != choice: # must remove the no prize door, so only the win door and choice door left
            after_choose = [win, choice]

        keep_win = (choice == win)
        if keep_win: # if keeping the choice wins
            k_win += 1

        switch_choice = [d for d in after_choose if d != choice][0]
        switch_win = (switch_choice == win)
        if switch_win: # if switching the choice wins
            s_win += 1
    return f"If you dont switch, you win {k_win} times. If you switch, you win {s_win} times"


the_game()
