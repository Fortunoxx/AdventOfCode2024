def get_values(fileInfo):
    file = open(fileInfo["file"]).readlines()
    left = [int(line.split()[0]) for line in file]
    right = [int(line.split()[1]) for line in file]
    return (left, right)


def calc(left, right):
    return sum([abs(sorted(left)[i] - sorted(right)[i]) for i in range(len(left))])


def calc2(left, right):
    return sum([(l * right.count(l)) for l in left])


def solve_part1(fileInfo):
    (left, right) = get_values(fileInfo)
    return calc(left, right)


def solve_part2(fileInfo):
    (left, right) = get_values(fileInfo)
    return calc2(left, right)
