import re

def get_values(fileInfo):
    lines = open(fileInfo["file"]).readlines()

    re_pattern = r'(mul\(\d+\,\d+\))'
    rec_pattern = re.compile(re_pattern, re.VERBOSE)
    
    results = []
    for line in lines:
        res = rec_pattern.findall(line)
        results.extend([[int(i) for i in item.replace("mul(","").replace(")","").split(",")] for item in res])
    return results


def calc_part_1(items):
    return sum([item[0]*item[1] for item in items])


def solve_part1(fileInfo):
    return calc_part_1(get_values(fileInfo))


def solve_part2(fileInfo):
    items = get_values(fileInfo)
    return 0
