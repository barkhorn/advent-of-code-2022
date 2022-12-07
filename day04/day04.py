
def extract_ranges(s: str) -> tuple[tuple[int, int], tuple[int, int]]:
    r1, r2 = s.strip().split(',')
    r1s, r1e = r1.split('-')
    r2s, r2e = r2.split('-')
    return (int(r1s), int(r1e)), (int(r2s), int(r2e))


def is_contained(smaller: tuple[int, int], larger: tuple[int, int]) -> bool:
    return smaller[0] >= larger[0] and smaller[1] <= larger[1]


def does_overlap(r1: tuple[int, int], r2: tuple[int, int]) -> bool:
    return (r2[0] <= r1[0] <= r2[1]) or (r1[0] <= r2[0] <= r1[1])


if __name__ == '__main__':
    with open("day04.txt") as f:
        data = f.readlines()
    ranges = [extract_ranges(s) for s in data]
    contained_ranges = [is_contained(r1, r2) or is_contained(r2, r1) for r1, r2 in ranges]
    totals1 = sum([1 if r else 0 for r in contained_ranges])
    print(f"part 1: {totals1=}")
    overlaps = [1 if does_overlap(*r) else 0 for r in ranges]
    print(f"part 2: {sum(overlaps)=}")
