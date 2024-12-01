# TODO: Implement this function
def get_values(fileInfo, n=1):
    left = []
    right = []

    with open(fileInfo["file"]) as file:
        for line in file:
            line = line.replace("\n", "")
            line = line.replace("   ", ";")
            parts = line.split(";")
            left.append(int(parts[0]))
            right.append(int(parts[1]))

            left.sort()
            right.sort()

        return (left, right)


def calc(left, right):
    deltas = []
    for i in range(len(left)):
        deltas.append(abs(left[i] - right[i]))

    return sum(deltas)

def calc2(left, right):
    return 0 # todo


def solve_part1(fileInfo):
    (left, right) = get_values(fileInfo)
    return calc(left, right)


def solve_part2(fileInfo):
    (left, right) = get_values(fileInfo)
    return calc2(left, right)
