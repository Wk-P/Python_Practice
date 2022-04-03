from cs1robots import *

load_world('./worlds/harvest3.wld')
hubo = Robot(beepers=10)
hubo.set_trace('blue')


def turn_right():
    for i in range(3):
        hubo.turn_left()


def pick_move():
    if not hubo.on_beeper():
        hubo.drop_beeper()
    hubo.move()


def main():
    pick_move()
    for i in range(3):
        for i in range(5):
            pick_move()
        hubo.turn_left()
        pick_move()
        hubo.turn_left()
        for i in range(5):
            pick_move()
        if hubo.get_pos() == (2, 6):
            hubo.drop_beeper()
            break
        turn_right()
        pick_move()
        turn_right()


if __name__ == "__main__":
    main()
