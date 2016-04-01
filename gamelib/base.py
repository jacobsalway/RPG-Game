class Director:
    def __init__(self, states, data):
        self.states = states
        self.data = data
        self.current_state = 0

        self.event_handlers = []

        for x in self.data:
            x.director = self

            self.event_handlers.append({'module': x.name, 'keyword': x.event})

        for x in self.states:
            x.director = self

    def run_logic(self):
        # command = input('~: ')

        # split_command = command.strip().split(' ')

        # for thing in split_command:
        #     if thing == 'switch':
        #         print('Switched!')

        #         self.current_state += 1

        #         if self.current_state >= len(self.states):
        #             self.current_state = 0
        #     elif thing == 'current':
        #         print(self.states[self.current_state].name)
        #     elif thing == 'list':
        #         for thing in self.data:
        #             print(thing.data)
        #     elif thing == 'map':
        #         self.get_module('map').run_module(self.get_module('pos').data)
        #     else:
        #         return_value = self.states[self.current_state].run_state(thing)

        #         self.handle_return(return_value)

        # Run pre-loop binds here

        # Get input and remove trailing whitespace
        command = input('~: ').strip()

        # Define the queue where end of loop events will resolve
        end_queue = []

        # Check for overriding commands
        if command == 'exit':
            exit()

        # Split command by keyword and other data
        split_command = command.split(' ')

        # Check if there is a relevant handler for this keyword
        # Always check modules first
        if self.has_handler(split_command[0]):
            return_value = self.get_handler(split_command[0]).handle_command(split_command)

            end_queue.append(return_value)
        else:
            print('No handler.')

        # Add return value to processing queue
        # Take and process the return value
        # i.e update modules

        print(end_queue)

        for item in end_queue:
            if item is not None:
                if 'command' in item:
                    print('command is in item!')

    def handle_return(self, return_value):
        if return_value['command'] == 'update':
            if self.get_module(return_value['module']) is not False:
                self.get_module(return_value['module']).update_data(return_value['data'])

    def get_module(self, module_name):
        for data in self.data:
            if data.name == module_name:
                return data

        return False

    def has_handler(self, command):
        for x in self.event_handlers:
            if x['keyword'] == command:
                return True

        return False

    def get_handler(self, keyword):
        for x in self.event_handlers:
            if keyword == x['keyword']:
                return self.get_module(x['module'])


# Base game object class
class GameObject:
    def __init__(self, name):
        self.name = name

    def handle_command(self, command):
        pass


class State(GameObject):
    def __init__(self, name):
        super().__init__(name)

    def run_state(self, command):
        pass


class Module(GameObject):
    def __init__(self, name, data, event = None):
        super().__init__(name)

        self.data = data
        self.event = event

    def update_data(self, data):
        pass

    def return_data(self, key):
        return self.data[key]

    def bind_event(self):
        return self.event


class Event:
    def __init__(self, event_type, content):
        self.type = event_type
        self.content = content


# class EventHandler:
#     def __init__(self, event, callback):
