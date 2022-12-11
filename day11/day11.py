import math


def monkey_business(rounds=20, increased_worry=False):
    monkey_inventories = [
        [72, 97],
        [55, 70, 90, 74, 95],
        [74, 97, 66, 57],
        [86, 54, 53],
        [50, 65, 78, 50, 62, 99],
        [90],
        [88, 92, 63, 94, 96, 82, 53, 53],
        [70, 60, 71, 69, 77, 70, 98]
    ]
    monkey_ops = (
        lambda x: x * 13,
        lambda x: x * x,
        lambda x: x + 6,
        lambda x: x + 2,
        lambda x: x + 3,
        lambda x: x + 4,
        lambda x: x + 8,
        lambda x: x * 7
    )
    monkey_mods = (
        19,
        7,
        17,
        13,
        11,
        2,
        5,
        3
    )
    monkey_mods_lcm = math.lcm(*monkey_mods)
    monkey_targets = (
        (5, 6),
        (5, 0),
        (1, 0),
        (1, 2),
        (3, 7),
        (4, 6),
        (4, 7),
        (2, 3)
    )
    monkey_activity = [0 for _ in range(len(monkey_inventories))]
    for _ in range(rounds):
        for i in range(len(monkey_inventories)):
            for item in monkey_inventories[i]:
                worry_level = (monkey_ops[i](item) % monkey_mods_lcm) if increased_worry else (monkey_ops[i](item) // 3)
                m1, m2 = monkey_targets[i]
                target = m1 if worry_level % monkey_mods[i] == 0 else m2
                monkey_inventories[target].append(worry_level)
                monkey_activity[i] += 1
            monkey_inventories[i] = []
    monkey_activity.sort()
    return monkey_activity[-1] * monkey_activity[-2]


if __name__ == '__main__':
    act = monkey_business()
    print(act)
    act2 = monkey_business(rounds=10000, increased_worry=True)
    print(act2)
