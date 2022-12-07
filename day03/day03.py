
def generate_priorities():
    def char_range(c1, c2):
        for c in range(ord(c1), ord(c2) + 1):
            yield chr(c)
    p = {k: v for (k, v) in zip(char_range('a', 'z'), range(1, 27))}
    p2 = {k: v for (k, v) in zip(char_range('A', 'Z'), range(27, 53))}
    return p | p2


Priorities = generate_priorities()


def split_compartments(s: str) -> tuple[str, str]:
    i = len(s) // 2
    return s[:i], s[i:]


def find_errors(lst1: str, lst2: str) -> list[str]:
    return [value for value in set(lst1) if value in lst2]


def iterate_groups(d: list[str]) -> list[tuple[str, str, str]]:
    for i in range(len(d) // 3):
        yield d[i*3], d[i*3 + 1], d[i*3 + 2]


def find_common_type(group1: str, group2: str, group3: str) -> list[str]:
    return [value for value in set(group1.strip()) if value in group2 and value in group3]


if __name__ == '__main__':
    with open("day03.txt") as f:
        data = f.readlines()
    errors = [find_errors(*split_compartments(s)) for s in data]
    priorities = [Priorities[e] for s in errors for e in s]
    print(f"part 1: {sum(priorities)=}")
    common_types = [find_common_type(*g) for g in iterate_groups(data)]
    priorities2 = [Priorities[ct] for s in common_types for ct in s]
    print(f"part 2: {sum(priorities2)=}")
