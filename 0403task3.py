from cs1robots import *

# change the map name to test
load_world('./worlds/hurdles3.wld')
hubo = Robot()
hubo.set_trace('blue')


def turn_right():
    for i in range(3):
        hubo.turn_left()


def detours():
    hubo.turn_left()
    hubo.move()
    turn_right()
    hubo.move()
    turn_right()
    hubo.move()
    hubo.turn_left()


def main():
    while not hubo.on_beeper():
        if not hubo.front_is_clear():
            detours()
        else:
            hubo.move()


if __name__ == "__main__":
    main()
