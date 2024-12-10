def get_values(fileInfo, result=[]):
    input = [int(char) for char in open(fileInfo["file"]).readline() if char != "\n"]
    for idx, i in enumerate(input):
        if idx % 2 == 0:
            result.extend([int((idx / 2)) for _ in range(i)])
        else:
            result.extend([None for _ in range(i)])

    # calc gaps and valid values
    gaps = [idx for idx, i in enumerate(result) if i is None]
    valid = [i for i in result if i is not None]
    return (valid, gaps)


def order_values(valid, gaps):
    for idx in gaps:
        valid.insert(idx, valid.pop())
    return valid


def calc_checksum(items):
    return sum([idx * i for idx, i in enumerate(items)])


def solve_part1(fileInfo):
    (valid, gaps) = get_values(fileInfo)
    return sum([idx * i for idx, i in enumerate(order_values(valid, gaps))])


def solve_part2(fileInfo):
    return 0
