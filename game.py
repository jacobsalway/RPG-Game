from gamelib import base
from gamelib import states
from gamelib import modules


def main():
    state_1 = states.MovementState('State 2')
    pos_module = modules.pos()
    map_module = modules.map()
    director = base.Director([state_1], [pos_module, map_module])

    quit_flag = False

    while not quit_flag:
        director.run_logic()

if __name__ == '__main__':
    main()
