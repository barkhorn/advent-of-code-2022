
def is_visible(grid, x, y):
    if x == 0 or y == 0:
        return True
    if x == len(grid[0]) - 1:
        return True
    if y == len(grid) - 1:
        return True
    height = grid[y][x]
    from_left_side = [grid[y][i] < height for i in range(0, x)]
    from_right_side = [grid[y][i] < height for i in range(x + 1, len(grid[0]))]
    from_top_side = [grid[i][x] < height for i in range(0, y)]
    from_bottom_side = [grid[i][x] < height for i in range(y + 1, len(grid))]
    return any([
        all(from_left_side),
        all(from_right_side),
        all(from_top_side),
        all(from_bottom_side)
    ])


def score(g, x, y):
    if x == 0 or y == 0:
        return 0
    if x == len(g[0]) - 1:
        return 0
    if y == len(g) - 1:
        return 0
    s_left = 1
    while x - s_left > 0 and g[y][x - s_left] < g[y][x]:
        s_left += 1
    s_right = 1
    while x + s_right < len(g[0]) - 1 and g[y][x + s_right] < g[y][x]:
        s_right += 1
    s_top = 1
    while y - s_top > 0 and g[y - s_top][x] < g[y][x]:
        s_top += 1
    s_bottom = 1
    while y + s_bottom < len(g) - 1 and g[y + s_bottom][x] < g[y][x]:
        s_bottom += 1
    return s_left * s_right * s_top * s_bottom


def scenic_scores(g):
    return [[score(g, x, y) for x in range(len(g[0]))] for y in range(len(g))]


if __name__ == '__main__':
    with open("day08.txt") as f:
        data = f.readlines()
    grid = [[int(col) for col in line.strip()] for line in data]
    total_visible = sum([1 if is_visible(grid, x, y) else 0
                         for x in range(len(grid[0])) for y in range(len(grid))])
    print(f"{total_visible=}")
    print(f"{max((i for r in scenic_scores(grid) for i in r))=}")
