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

        return (left, right)


def calc(left, right):
    # this array will hold the numbers
    deltas = []

    left.sort()
    right.sort()

    # for each item, find the difference between the number pairs
    for i in range(len(left)):
        deltas.append(abs(left[i] - right[i]))

    return sum(deltas)

def calc2(left, right):
    # this array will hold the numbers
    results = []

    # for each value, find the number of times it appears in right
    for l in left:
        results.append(l * right.count(l))

    # return the sum of the results
    return sum(results)


def solve_part1(fileInfo):
    (left, right) = get_values(fileInfo)
    return calc(left, right)


def solve_part2(fileInfo):
    (left, right) = get_values(fileInfo)
    return calc2(left, right)
