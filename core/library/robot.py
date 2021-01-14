class Robot:
    def __init__(self):
        self.move_items = {
            'Left': 'l',
            'Right': 'r',
            'Up': 'u',
            'Down': 'd',
            'Paint': 'p'
        }
        self.moves = []

    def route_move(self, type_move):
        if type_move == 'end':
            return self.moves
        self.moves.append(self.move_items[type_move])

    
