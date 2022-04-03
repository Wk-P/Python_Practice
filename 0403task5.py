from cs1robots import *

m = int(input("rows: "))
n = int(input("columns: "))
create_world(m, n)
hubo = Robot()
hubo.set_trace('blue')


def turn_right():
    for i in range(3):
        hubo.turn_left()


def robot_move():
    while hubo.front_is_clear():
        hubo.move()


def circle():
    hubo.turn_left()
    robot_move()
    turn_right()
    if not hubo.front_is_clear():
        return False
    hubo.move()
    turn_right()
    robot_move()
    hubo.turn_left()
    if not hubo.front_is_clear():
        return False
    hubo.move()
    return True


def main():
    while circle():
        continue


if __name__ == "__main__":
    main()