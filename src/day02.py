def get_values(fileInfo):
    file = open(fileInfo["file"]).readlines()
    return [[int(item) for item in line.split()] for line in file]


def check(a, b, direction, min_diff=1, max_diff=3):
    if direction == "up":
        return a < b and b - a >= min_diff and b - a <= max_diff
    elif direction == "down":
        return a > b and a - b >= min_diff and a - b <= max_diff
    else:
        return False


def check_record(record):
    previous = None
    direction = None
    fault = False
    idx = 0

    for id, i in enumerate(record):
        if previous is None:
            previous = i
            continue
        else:
            if previous < i and direction is None:
                direction = "up"
            elif previous > i and direction is None:
                direction = "down"
            if previous == i:
                fault = True
                idx = id
                break
            if not check(previous, i, direction):
                fault = True
                idx = id
                break
        previous = i
    return (not fault, idx)


def calc_part_1(items, counter=0):
    for record in items:
        (is_valid, _) = check_record(record)
        counter += 1 if is_valid else 0
    return counter


def calc_part_2(items, counter=0):
    for record in items:
        (is_valid, idx) = check_record(record)
        is_valid_2 = True
        is_valid_1 = True

        if is_valid:
            counter += 1
        else:
            new_record1 = record.copy()
            new_record2 = record.copy()
            new_record3 = record.copy()

            new_record1.pop(idx)
            new_record2.pop(idx - 1)
            if(idx - 2 >= 0):
                new_record3.pop(idx - 2)

            (is_valid_1, _) = check_record(new_record1)
            (is_valid_2, _) = check_record(new_record2)
            (is_valid_3, _) = check_record(new_record3)

            counter += 1 if is_valid_1 or is_valid_2 or is_valid_3 else 0
    return counter


def solve_part1(fileInfo):
    items = get_values(fileInfo)
    return calc_part_1(items)


def solve_part2(fileInfo):
    items = get_values(fileInfo)
    return calc_part_2(items)
