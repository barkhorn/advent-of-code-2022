
line_width = 40
x = 1
clock = 0
signal_strenghts = []
crt = ['.' for _ in range(line_width*6)]


def tick():
    global clock, signal_strenghts, crt
    if abs(clock % line_width - x) < 2:
        crt[clock] = '#'
    clock += 1
    if clock in (20, 60, 100, 140, 180, 220):
        signal_strenghts.append(x * clock)


def run_simulation(lines: list[str]):
    global x
    for line in lines:
        match line.strip().split():
            case "noop", : tick()
            case "addx", i:
                tick()
                tick()
                x += int(i)


if __name__ == '__main__':
    with open("day10.txt") as f:
        data = f.readlines()
    run_simulation(data)
    print(f"{sum(signal_strenghts)=}")
    for row in range(0, line_width*6, line_width):
        print(''.join(crt[row:row+line_width]))
