def turn_right():
    turn_left()
    turn_left()
    turn_left()
def turn_180degrees():
     turn_left()
     turn_left()
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif right_is_clear()== False and front_is_clear():
        move()
    else:
        turn_180degrees()
       
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
