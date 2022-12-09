PRINT_MOVES = False


def print_grid(visited, hx=0, hy=0, tx=0, ty=0, draw_visited=True):
    size = max(max(x, y) for x, y in visited) + 1
    for y in range(size, -1, -1):
        for x in range(0, size):
            c = '.'
            if draw_visited and (x, y) in visited:
                c = '#'
            if x == 0 and y == 0:
                c = 's'
            if tx == x and ty == y:
                c = 'T'
            if hx == x and hy == y:
                c = 'H'
            print(c, end='')
        print()


def apply_moves(moves: list[str], start: tuple[int, int] = (0, 0)):
    hx, hy = start
    tx, ty = start
    visited = set()

    def update_tail():
        nonlocal visited, tx, ty
        dx = hx - tx
        dy = hy - ty
        if abs(dx) > 1 or abs(dy) > 1:  # need to move tail
            if dx != 0 and dy != 0:  # diagonal
                tx = tx + (1 if dx > 0 else -1)
                ty = ty + (1 if dy > 0 else -1)
            else:  # only x or y move
                if dx != 0:
                    tx = tx + (1 if dx > 0 else -1)
                if dy != 0:
                    ty = ty + (1 if dy > 0 else -1)
        visited.add((tx, ty))
        if PRINT_MOVES:
            print_grid(visited, hx, hy, tx, ty, draw_visited=False)
            print()

    for move in moves:
        match move.strip().split():
            case 'R', i:
                for _ in range(int(i)):
                    hx += 1
                    update_tail()
            case 'L', i:
                for _ in range(int(i)):
                    hx -= 1
                    update_tail()
            case 'U', i:
                for _ in range(int(i)):
                    hy += 1
                    update_tail()
            case 'D', i:
                for _ in range(int(i)):
                    hy -= 1
                    update_tail()
            case _: raise RuntimeError(f"unknown move: {move}")
    return visited


if __name__ == '__main__':
    with open("day09.txt") as f:
        data = f.readlines()
    tail_visited = apply_moves(data)
    # print_grid(tail_visited)
    print(len(tail_visited))
