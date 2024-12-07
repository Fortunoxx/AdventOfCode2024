def get_values(fileInfo):
    with open(fileInfo["file"], "r") as f:
        result = []
        for line in f.readlines():
            left, right = line.split(":")
            obj = {"result": int(left), "values": [int(x) for x in right.split()]}
            result.append(obj)
    return result


def is_valid(result, values, is_part_2=False):
    return calc_next(values[0], values[1:], result, is_part_2)


def calc_next(current, remaining, target, is_part_2=False):
    if not remaining:
        return current == target
    next_value = remaining[0]
    if not is_part_2:
        return calc_next(current + next_value, remaining[1:], target) or calc_next(
            current * next_value, remaining[1:], target
        )
    return (
        calc_next(current + next_value, remaining[1:], target, is_part_2)
        or calc_next(current * next_value, remaining[1:], target, is_part_2)
        or calc_next(int(str(current) + str(next_value)), remaining[1:], target, is_part_2)
    )


def solve_part1(fileInfo):
    items = get_values(fileInfo)
    valid = [
        item["result"] for item in items if (is_valid(item["result"], item["values"]))
    ]
    return sum(valid)


def solve_part2(fileInfo):
    items = get_values(fileInfo)
    valid = [
        item["result"] for item in items if (is_valid(item["result"], item["values"], True))
    ]
    return sum(valid)
