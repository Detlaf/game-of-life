import random
import time

DEAD = 0
LIVE = 1

def dead_state(height, width):
    return [[DEAD for _ in range(width)] for _ in range(height)]

def random_state(height, width):
    board = [[DEAD if random.random() >= 0.5 else LIVE for _ in range(width)] for _ in range(height)]
    return board
    
def pretty_print(board):
    symbols = {
        DEAD: ".",
        LIVE: "@"
    }
    lines = []
    print(' - ' * len(board))
    for x in range(len(board)):
        line = ''
        for y in range(len(board[0])):
            line += symbols[board[x][y]]
        lines.append(line)
    print("\n".join(lines))

    print(' - ' * len(board))


def next_board_state(current_state):
    height = len(current_state)
    width = len(current_state[0])
    new_state = dead_state(len(current_state), len(current_state[0]))
    for x in range(height):
        for y in range(width):
            live_neighbors = 0
            for x_ in range((x-1), (x+1)+1):
                if x_ < 0 or x_ >= height:
                    continue
                for y_ in range((y-1), (y+1)+1):
                    if y_ < 0 or y_ >= width:
                        continue
                    if x_ == x and y_ == y:
                        continue
                    if current_state[x_][y_] == LIVE:
                        live_neighbors += 1

            if current_state[x][y] == LIVE:
                if live_neighbors <= 1:
                    # underpopulation
                    new_state[x][y] = DEAD
                if live_neighbors == 2 or live_neighbors == 3:
                    # just right
                    new_state[x][y] = LIVE
                if live_neighbors > 3:
                    # overpopulation
                    new_state[x][y] = DEAD
            else:
                if live_neighbors == 3:
                    # reproduction
                    new_state[x][y] = LIVE
                else:
                    new_state[x][y] = DEAD
    return new_state   


if __name__ == '__main__':
    next_state = random_state(5, 10)
    while True:
        pretty_print(next_state)
        next_state = next_board_state(next_state)
        time.sleep(0.5)