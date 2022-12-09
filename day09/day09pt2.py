
def apply_moves(moves: list[str], start: tuple[int, int] = (0, 0)):
    hx, hy = start
    knots = [start for _ in range(9)]
    visited = set()

    def update_tail():
        nonlocal visited, knots
        _hx = hx
        _hy = hy
        for k_idx in range(len(knots)):
            tx, ty = knots[k_idx]
            dx = _hx - tx
            dy = _hy - ty
            if abs(dx) > 1 or abs(dy) > 1:  # need to move tail
                tx = tx + (1 if dx > 0 else -1 if dx < 0 else 0)
                ty = ty + (1 if dy > 0 else -1 if dy < 0 else 0)
                knots[k_idx] = (tx, ty)
            _hx = tx  # advance the chain. current tail becomes the head for the next tail
            _hy = ty
        visited.add(knots[-1])

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
    print(len(tail_visited))
