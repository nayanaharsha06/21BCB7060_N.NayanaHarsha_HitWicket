class Figure:
    def __init__(self, name, player, row, col):
        self.name = name
        self.player = player
        self.row = row
        self.col = col

    def movement(self, dr, dc, board):
        new_r, new_c = self.row + dr, self.col + dc
        if 0 <= new_r < 5 and 0 <= new_c < 5:
            if board[new_r][new_c] is None:
                board[self.row][self.col] = None
                self.row, self.col = new_r, new_c
                board[new_r][new_c] = self
                return True
        return False

class Pawn(Figure):
    def movement(self, direction, board):
        directions = {'L': (-1, 0), 'R': (1, 0), 'F': (0, -1), 'B': (0, 1)}
        if direction in directions:
            dr, dc = directions[direction]
            return super().movement(dr, dc, board)
        return False

class Hero1(Figure):
    def movement(self, direction, board):
        directions = {'L': (-2, 0), 'R': (2, 0), 'F': (0, -2), 'B': (0, 2)}
        if direction in directions:
            dr, dc = directions[direction]
            return super().movement(dr, dc, board)
        return False

class Hero2(Figure):
    def movement(self, direction, board):
        directions = {'L': (-2, -2), 'R': (2, -2), 'F': (-2, -2), 'B': (2, 2)}
        if direction in directions:
            dr, dc = directions[direction]
            return super().movement(dr, dc, board)
        return False

class Game:
    def __init__(self):
        self.board = [[None for _ in range(5)] for _ in range(5)]
        self.players = {'A': [], 'B': []}
        self.turn = 'A'

    def start_game(self):
        self.players['A'] = [Pawn('P1', 'A', 0, 4), Hero1('H1', 'A', 1, 4), Hero2('H2', 'A', 2, 4)]
        self.players['B'] = [Pawn('P1', 'B', 0, 0), Hero1('H1', 'B', 1, 0), Hero2('H2', 'B', 2, 0)]
        for piece in self.players['A']:
            self.board[piece.row][piece.col] = piece
        for piece in self.players['B']:
            self.board[piece.row][piece.col] = piece

    def move(self, player, figure_name, direction):
        if player != self.turn:
            return False
        for piece in self.players[player]:
            if piece.name == figure_name:
                if piece.movement(direction, self.board):
                    self.turn = 'B' if self.turn == 'A' else 'A'
                    return True
        return False

    def curr_board_state(self):
        return [[None if cell is None else f"{cell.player}--{cell.name}" for cell in row] for row in self.board]
