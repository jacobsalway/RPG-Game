from . import base


class pos(base.Module):
    def __init__(self):
        super().__init__('pos', {'x': 0, 'y': 0}, 'move')

        self.movement_library = {
            'up': [0, -1],
            'down': [0, 1],
            'left': [-1, 0],
            'right': [1, 0]
        }

    def handle_command(self, command):
        if command[0] == self.event:
            if command[1] in self.movement_library.keys():
                self.update_data(self.movement_library[command[1]])

    def update_data(self, data):
        self.data['x'] += data[0]
        self.data['y'] += data[1]


class map(base.Module):
    def __init__(self):
        super().__init__('map', ['aaaaa', 'bbbbb', 'ccccc'], 'map')

    def update_data(self, data):
        pass

    def handle_command(self, command):
        if command[0] == self.event:
            self.run_module()

    def run_module(self):
        x, y = 0, 0

        player_pos = {'x': 0, 'y': 0}
        player_pos['x'] = self.director.get_module('pos').return_data('x')
        player_pos['y'] = self.director.get_module('pos').return_data('y')

        for row in self.data:
            row_data = []
            for column in row:
                if x == player_pos['x'] and y == player_pos['y']:
                    column = 'P'
                row_data.append(column)
                x += 1
            x = 0

            row_print = ''

            for item in row_data:
                row_print += item

            print(row_print)
            y += 1
