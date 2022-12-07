
def grouped_calories(lines: list[str]):
    cals = 0
    for line in lines:
        if line.strip() == "":
            yield cals
            cals = 0
        else:
            cals += int(line)


if __name__ == '__main__':
    with open("day01.txt") as f:
        data = f.readlines()
    print(f"part 1: {max(grouped_calories(data))=}")
    top_3_elves = sorted(list(grouped_calories(data)))[-3:]
    print(f"part 2: {sum(top_3_elves)=}")
