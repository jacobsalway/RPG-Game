class Director:
    def __init__(self, states):
        self.states = states
        self.current_state = 0

    def run_logic(self):
        print('Enter a command')
        command = input('~: ')

        if command == 'switch':
            print('Switched!')

            self.current_state += 1

            if self.current_state >= len(self.states):
                self.current_state = 0
        elif command == 'current':
            print(self.states[self.current_state].name)
        else:
            return_value = self.states[self.current_state].run_state(command)

            print(return_value)


class State:
    def __init__(self, name):
        self.name = name

    def run_state(self, command):
        print('You executed ' + command + ' in ' + self.name + '!')

        return('Test data')
