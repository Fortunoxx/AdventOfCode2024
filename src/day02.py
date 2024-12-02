def get_values(fileInfo):
    file = open(fileInfo["file"]).readlines()
    items = [int(i) for i in [line.split() for line in file]]
    return items


def calc(items, max_diff=3):
    counter = 0

    for record in items:
        previous = None
        direction = None
        for i in record:
            if previous is None:
                previous = i
                continue
            else:
                if previous == i:
                    continue
                if previous < i:
                    if direction is None:
                        direction = "up"
                    elif direction is not "up":
                        continue
                    if(i - previous <= max_diff):
                        counter += 1
                else:
                    if direction is None:
                        direction = "down"
                    elif direction is not "down":
                        continue
                    if(previous - i <= max_diff):
                        counter += 1

                previous = i

    return counter


def solve_part1(fileInfo):
    items = get_values(fileInfo)
    return calc(items)


def solve_part2(fileInfo):
    return 0