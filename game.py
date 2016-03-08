from gamelib import base


def main():
    state_1 = base.State('State 1')
    state_2 = base.State('State 2')
    director = base.Director([state_1, state_2])

    quit_flag = False

    while not quit_flag:
        director.run_logic()

if __name__ == '__main__':
    main()
