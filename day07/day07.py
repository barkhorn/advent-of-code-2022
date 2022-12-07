

def sum_up_dirs(lines: list[str]):
    res = {}
    current_hierarchy = []
    for line in lines:
        match line.strip():
            case s if s.startswith("$ cd"):
                to = s.split(' ')[2]
                if to == '..':
                    current_hierarchy.pop()
                elif to == '/':
                    current_hierarchy = []
                else:
                    current_hierarchy.append(to)
            case s if s.startswith("$"):
                pass
            case _:
                for i in range(len(current_hierarchy) + 1):
                    path = '/' + "/".join(current_hierarchy[:i])
                    if not s.startswith('dir '):
                        old = 0 if res.get(path) is None else res[path]
                        res[path] = old + int(s.split(' ')[0])
    return res


def find_smallest_to_delete(sums: dict):
    fs_total = 70000000
    fs_desired_free = 30000000
    fs_current_free = fs_total - sums['/']
    need_to_delete = fs_desired_free - fs_current_free
    print(need_to_delete)
    candidates = [(sums[d], d) for d in sums if sums[d] > need_to_delete]
    return sorted(candidates)[0]


if __name__ == '__main__':
    with open("day07.txt") as f:
        data = f.readlines()
    sums = sum_up_dirs(data)
    sum_of_sm100000 = sum([sums[k] for k in sums if sums[k] < 100000])
    print(f"{sum_of_sm100000=}")
    to_del = find_smallest_to_delete(sums)
    print(f"{to_del=}")
