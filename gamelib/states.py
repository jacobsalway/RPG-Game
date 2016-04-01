from . import base


class MovementState(base.State):
    def run_state(self, command):
        super().run_state(command)

        delta = [0, 0]

        if command == 'right':
            delta[0] = 1
        elif command == 'left':
            delta[0] = -1
        elif command == 'up':
            delta[1] = -1
        elif command == 'down':
            delta[1] = 1

        return({'command': 'update', 'module': 'pos', 'data': delta})
