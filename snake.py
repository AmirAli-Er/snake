import consts


class Snake:
    # directions
    dx = {'UP': 0, 'DOWN': 0, 'LEFT': -1, 'RIGHT': 1}
    dy = {'UP': -1, 'DOWN': 1, 'LEFT': 0, 'RIGHT': 0}

    def __init__(self, keys, game, pos, color, direction):
        # keys which are pressed
        self.keys = keys
        # pos => head of snake
        self.cells = [pos]
        self.game = game
        self.game.add_snake(self)
        self.color = color
        self.direction = direction
        self.head = list(self.get_head())
        game.get_cell(pos).set_color(color)

    def get_head(self):
        return self.cells[-1]

    def val(self, x):
        if x < 0:
            x += self.game.size

        if x >= self.game.size:
            x -= self.game.size

        return x

    def next_move(self):
        next_pos = [self.val(self.cells[0][0] + Snake.dx[self.direction]),
                    self.val(self.cells[0][1] + Snake.dy[self.direction])]
        next_cell = self.game.get_cell(next_pos)
        if next_cell.color == consts.back_color :
            # crawling
            next_cell.set_color(self.color)
            self.cells.insert(0, (next_pos[0], next_pos[1]))
            tail = self.cells.pop()
            self.game.get_cell(tail).set_color(consts.back_color)
        elif next_cell.color == consts.fruit_color:
            # adding new block to the snake
            next_cell.set_color(self.color)
            self.cells.insert(0, (next_pos[0], next_pos[1]))
        else:
            # crash !
            self.game.kill(self)


    def handle(self, chars):
        for i in chars:
            x = self.keys.get(i, False)
            if x:
                if x == 'LEFT' and self.direction == 'RIGHT' or x == 'RIGHT' and self.direction == 'LEFT':
                    pass
                elif x == 'DOWN' and self.direction == 'UP' or x == 'UP' and self.direction == 'DOWN':
                    pass
                elif x == self.direction:
                    pass
                else:
                    self.direction = x
