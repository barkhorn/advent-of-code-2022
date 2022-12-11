import math


def monkey_business(rounds=20, increased_worry=False):
    monkey_inventories = [
        [79, 98],
        [54, 65, 75, 74],
        [79, 60, 97],
        [74]
    ]
    monkey_ops = (
        lambda x: x * 19,
        lambda x: x + 6,
        lambda x: x * x,
        lambda x: x + 3
    )
    monkey_mods = (
        23,
        19,
        13,
        17
    )
    monkey_mods_lcm = math.lcm(*monkey_mods)
    monkey_targets = (
        (2, 3),
        (2, 0),
        (1, 3),
        (0, 1)
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
    act = monkey_business(rounds=20)
    print(act)
    act2 = monkey_business(rounds=10000, increased_worry=True)
    print(act2)
