from enum import IntEnum


class Shape(IntEnum):
    Rock = 1
    Paper = 2
    Scissors = 3


class Strategy(IntEnum):
    Win = 1
    Draw = 2
    Loss = 3


def code2shape(inp: str) -> Shape:
    match inp.upper():
        case 'A' | 'X': return Shape.Rock
        case 'B' | 'Y': return Shape.Paper
        case 'C' | 'Z': return Shape.Scissors


def code2strategy(inp: str) -> Strategy:
    match inp.upper():
        case 'X': return Strategy.Loss
        case 'Y': return Strategy.Draw
        case 'Z': return Strategy.Win


def game_score(elf: Shape, me: Shape) -> int:
    loss = 0
    draw = 3
    win = 6
    match (elf, me):
        case (Shape.Rock, Shape.Paper): return win
        case (Shape.Paper, Shape.Scissors): return win
        case (Shape.Scissors, Shape.Rock): return win
        case (x, y) if x == y: return draw
        case _: return loss


def score4round(coded: str) -> int:
    tokens = coded.strip().split(' ')
    elf = code2shape(tokens[0])
    me = code2shape(tokens[1])
    score = me.value + game_score(elf, me)
    return score


def score4round_part2(coded: str) -> int:
    tokens = coded.strip().split(' ')
    elf = code2shape(tokens[0])
    match code2strategy(tokens[1]):
        case Strategy.Win:
            if elf == Shape.Paper:
                me = Shape.Scissors
            if elf == Shape.Scissors:
                me = Shape.Rock
            if elf == Shape.Rock:
                me = Shape.Paper
        case Strategy.Draw: me = elf
        case Strategy.Loss:
            if elf == Shape.Paper:
                me = Shape.Rock
            if elf == Shape.Scissors:
                me = Shape.Paper
            if elf == Shape.Rock:
                me = Shape.Scissors
    score = me.value + game_score(elf, me)
    print(f"{elf=}, {me=}, {score=}")
    return score


if __name__ == '__main__':
    with open("day02.txt") as f:
        data = f.readlines()
    total_score = sum([score4round(r) for r in data])
    print(f"part 1: {total_score=}")
    total_score_part2 = sum([score4round_part2(r) for r in data])
    print(f"part 2: {total_score_part2=}")
