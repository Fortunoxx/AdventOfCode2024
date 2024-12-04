def get_values(fileInfo):
    with open(fileInfo["file"], 'r') as file:
        return {
            (x, y): char
            for y, line in enumerate(file)
            for x, char in enumerate(line)
            if char != "\n"
        }

def find_coordinates(items, char):
    return [key for key, value in items.items() if value == char]


def all_directions():
    return [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1)
    ]


def find_occurences(items, coordinates, word):
    occurences = []
    for coordinate in coordinates:
        for direction in all_directions():
            occurence = []
            for i in range(0, len(word)):
                x = coordinate[0] + direction[0] * i
                y = coordinate[1] + direction[1] * i

                if (x, y) in items:
                    occurence.append(items[(x, y)])
                else:
                    break
            if "".join(occurence) == word:
                occurences.append(coordinate)
    return occurences


def solve_part1(fileInfo):
    items = get_values(fileInfo)
    coordinates = find_coordinates(items, 'X')
    occurences = find_occurences(items, coordinates, 'XMAS')
    return len(occurences)


def solve_part2(fileInfo):
    return calc_part_1(get_values(fileInfo))
