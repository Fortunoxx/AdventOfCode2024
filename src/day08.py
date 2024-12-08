def get_values(fileInfo):
    with open(fileInfo["file"], "r") as file:
        content = {
            (x, y): char
            for y, line in enumerate(file)
            for x, char in enumerate(line)
            if char != "\n" and char != "."
        }

    with open(fileInfo["file"], "r") as file:
        lines = file.readlines()
        height = len(lines)
        width = max(len(line.strip()) for line in lines)
    return (content, width, height)


def transform(content, result={}):
    for key in content.keys():
        if content[key] not in result:
            result[content[key]] = [key]
        else:
            result[content[key]].append(key)
    return result


def calculate_all_antinode_locations(content, result=[]):
    for key in content.keys():
        result.extend(calculate_antinode_locations(content[key]))
    return list(set(result))


def calculate_all_antinode_locations_part2(content, width, height, result=[]):
    for key in content.keys():
        result.extend(calculate_antinode_locations_part2(content[key], width, height))
    return list(set(result))


def calculate_antinode_locations(locations):
    result = []
    for location1 in locations:
        for location2 in locations:
            if location1 == location2:
                continue
            antinode_locations = calculate_antinode_location(location1, location2)
            for location in antinode_locations:
                if location not in result:
                    result.append(location)
    return result


def calculate_antinode_locations_part2(locations, width, height):
    result = []
    for location1 in locations:
        if location1 not in result:
            result.append(location1)
        for location2 in locations:
            if location2 not in result:
                result.append(location2)
            if location1 == location2:
                continue
            antinode_locations = calculate_antinode_location_part2(location1, location2, width, height)
            for location in antinode_locations:
                if location not in result:
                    result.append(location)
    return result


def calculate_antinode_location(location1, location2):
    loc = []
    loc.append(
        (
            location1[0] - (location1[0] - location2[0]) * 2,
            location1[1] - (location1[1] - location2[1]) * 2,
        )
    )
    loc.append(
        (
            location2[0] - (location2[0] - location1[0]) * 2,
            location2[1] - (location2[1] - location1[1]) * 2,
        )
    )
    return loc


def calc_next(location1, location2, i=0):
    return (
        location1[0] - (location1[0] - location2[0]) * (i + 1),
        location1[1] - (location1[1] - location2[1]) * (i + 1),
    )


def calculate_antinode_location_part2(location1, location2, max_x, max_y):
    loc = []

    i = 1
    next = calc_next(location1, location2)
    while next[0] >= 0 and next[0] < max_x and next[1] >= 0 and next[1] < max_y:
        loc.append(next)
        next = calc_next(location1, location2, i)
        i += 1

    i = 1
    next = calc_next(location2, location1)
    while next[0] >= 0 and next[0] < max_x and next[1] >= 0 and next[1] < max_y:
        loc.append(next)
        next = calc_next(location2, location1, i)
        i += 1

    return loc


def solve_part1(fileInfo):
    (items, width, height) = get_values(fileInfo)
    trans = transform(items)
    anods = calculate_all_antinode_locations(trans)
    anod_filtered = [
        anod
        for anod in anods
        if anod[0] >= 0 and anod[0] < width and anod[1] >= 0 and anod[1] < height
    ]
    return len(anod_filtered)


def solve_part2(fileInfo):
    (items, width, height) = get_values(fileInfo)
    trans = transform(items)
    anods = calculate_all_antinode_locations_part2(trans, width, height)
    anod_filtered = [
        anod
        for anod in anods
        if anod[0] >= 0 and anod[0] < width and anod[1] >= 0 and anod[1] < height
    ]
    return len(anod_filtered)
