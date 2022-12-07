import re


def parse_stacks(nstacks: int, sdata: list[str]):
    res = [[] for _ in range(nstacks)]
    for s in reversed(sdata):
        for i in range(nstacks):
            idx = i * 4 + 1
            if len(s) > idx and s[idx].strip() != '':
                res[i] += s[idx]
    return res


def parse_move(move: str) -> tuple[int, int, int]:
    m = re.match("move (\\d+) from (\\d+) to (\\d+)", move)
    return int(m.group(1)), int(m.group(2)), int(m.group(3))


def apply_moves(st: list[list[str]], mv: list[tuple[int, int, int]]):
    for cnt, fr, to in mv:
        for _ in range(cnt):
            st[to - 1].append(st[fr - 1].pop())


def apply_moves_preserving_order(st: list[list[str]], mv: list[tuple[int, int, int]]):
    for cnt, fr, to in mv:
        buffer = [st[fr - 1].pop() for _ in range(cnt)]
        for crate in reversed(buffer):
            st[to - 1].append(crate)


def top_elements(st: list[list[str]]):
    return "".join([stack[len(stack)-1] for stack in st])


if __name__ == '__main__':
    with open("day05.txt") as f:
        data = f.readlines()
    stacks_end_index = 0
    while not data[stacks_end_index].strip().startswith("1   2   3"):
        stacks_end_index += 1
    moves = [parse_move(s.strip()) for s in data[stacks_end_index+2:]]
    stacks = parse_stacks(len(data[stacks_end_index].split()), data[:stacks_end_index])
    apply_moves(stacks, moves)
    print(f"part 1: {top_elements(stacks)=}")
    stacks2 = parse_stacks(len(data[stacks_end_index].split()), data[:stacks_end_index])
    apply_moves_preserving_order(stacks2, moves)
    print(f"part 2: {top_elements(stacks2)=}")
