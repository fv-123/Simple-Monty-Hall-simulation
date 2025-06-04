'''The core idea is to understand that the game master's action is not random (if you choose the wrong door). If you choose the wrong door,
which you definitely have a higher chance of doing, the game master has no choice but the remove the remaining wrong door, 
so if you switch in this case, you win. However, if you choose the right door from the start (1/3 chance), the game master 
can remove whatever door he wants. My point is that we should have the perspective that our initial choice is wrong,
since we have a higher chance to lose. That way we will always win when that 2/3 chance favors us.
Ultimately, you WIN when you LOSE (2/3) and you LOSE when you WIN (1/3).
Oh, and you can just count all possibilities but that goes to shit when you have 100 doors.'''

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
