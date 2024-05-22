# Short text-based game, multiple choices

from backend import * 
startGame()

path = intro()
if path == 1:
    second_path = path1()
    if second_path == 1:
        outcome = path1_1()
        ending(outcome)
    else:
        outcome = path1_2()
        ending(outcome)
elif path == 2:
    second_path = path2()
    if second_path == 1:
        outcome = path2_1()
        ending(outcome)
    else:
        outcome = path2_2()
        ending(outcome)
elif path == 3:
    outcome = path3()
    ending(outcome)
