import time
from cs1robots import *

# change the map to test
load_world('./worlds/harvest4.wld')
hubo = Robot()
hubo.set_trace('blue')


def turn_right():
    for i in range(3):
        hubo.turn_left()


def pick_move():
    while hubo.on_beeper():
        hubo.pick_beeper()
    hubo.move()


def main():
    pick_move()
    for i in range(3):
        time.sleep(0.5)
        for i in range(5):
            time.sleep(0.5)
            pick_move()
        time.sleep(0.5)
        hubo.turn_left()
        time.sleep(0.5)
        pick_move()
        time.sleep(0.5)
        hubo.turn_left()
        for i in range(5):
            time.sleep(0.5)
            pick_move()
        if hubo.get_pos() == (2, 6):
            break
        time.sleep(0.5)
        turn_right()
        time.sleep(0.5)
        pick_move()
        time.sleep(0.5)
        turn_right()


if __name__ == "__main__":
    main()
