import time
import keyboard
import mouse
import util

num = 1

timer = 50
timer2 = 20
mouse1 = 0
mouse2 = 0

saved_state = "waiting", mouse1, mouse2
state = "waiting", mouse1, mouse2

while timer > 0:
    while keyboard.is_pressed('shift') and timer2 > 0:
        if keyboard.is_pressed('1'):
            mouse1 = mouse.get_position()
        if keyboard.is_pressed('2'):
            mouse2 = mouse.get_position()
        state = "active", mouse1, mouse2
        if state != saved_state:
            saved_state = state
            print(state)

        timer2 = timer2 - 1
        time.sleep(0.05)
    else:
        state = "waiting", mouse1, mouse2
        if state != saved_state:
            saved_state = state
            print(state)
    timer2 = 20

    if mouse1 and mouse2:
        p1 = (min(mouse1[0], mouse2[0]), min(mouse1[1], mouse2[1]))
        p2 = (max(mouse1[0], mouse2[0]), max(mouse1[1], mouse2[1]))
        print(p1, p2)
        new_image = util.grab_snippet(p1, p2)
        print("success", new_image)
        break

    timer = timer - 1
    time.sleep(0.2)

