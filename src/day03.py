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


def get_values2(fileInfo):
    bigline = ""
    for line in open(fileInfo["file"]).readlines():
        bigline += line

    pattern1 = r'(don\'t\(\))'
    matches1 = re.finditer(pattern1, bigline)
    indexes1 = [match.start() for match in matches1]

    pattern2 = r'(do\(\))'
    matches2 = re.finditer(pattern2, bigline)
    indexes2 = [0]
    indexes2.extend([match.start() for match in matches2])

    indexes = []
    for do in indexes2:
        found = False
        for dont in indexes1:
            if dont > do and (len(indexes) == 0 or indexes[-1][1] < do):
                indexes.append((do, dont))
                found = True
                break
        if found:
            continue

    if(indexes2[-1] > indexes1[-1]):
        indexes.append((indexes2[-1], len(bigline)))

    # calc parts
    parts = [bigline[start:end] for (start, end) in indexes]

    # calc results
    re_pattern = r'(mul\(\d+\,\d+\))'
    rec_pattern = re.compile(re_pattern, re.VERBOSE)

    ret = []
    for part in parts:
        res = rec_pattern.findall(part)
        ret.extend([[int(i) for i in item.replace("mul(","").replace(")","").split(",")] for item in res])
    return ret


def calc_part_1(items):
    return sum([item[0]*item[1] for item in items])


def solve_part1(fileInfo):
    return calc_part_1(get_values(fileInfo))


def solve_part2(fileInfo):
    return calc_part_1(get_values2(fileInfo))
