def get_values(fileInfo, start_char="^"):
    with open(fileInfo["file"], "r") as file:
        content = {
            (x, y): char
            for y, line in enumerate(file)
            for x, char in enumerate(line)
            if char != "\n"
        }
    obstacles = [pos for pos, char in content.items() if char == "#"]
    start = [pos for pos, char in content.items() if char == start_char][0]
    width = max([pos[0] for pos in content.keys()])
    height = max([pos[1] for pos in content.keys()])
    return (obstacles, start, width, height)


# gets directions: starting with up, clockwise
def get_directions():
    return [(0, -1), (1, 0), (0, 1), (-1, 0)]


def add_tuples(tuple1, tuple2):
    return tuple(a + b for a, b in zip(tuple1, tuple2))


def move(obstacles, start, width, height):
    directions = get_directions()
    current = start
    current_direction = directions[0]
    visited = [start]
    while 0 <= current[0] <= width and 0 <= current[1] <= height:
        # calc next position
        next_position = add_tuples(current, current_direction)

        # check if out of bounds
        if (
            next_position[0] < 0
            or next_position[0] > width
            or next_position[1] < 0
            or next_position[1] > height
        ):
            break

        while next_position in obstacles:
            idx = (directions.index(current_direction) + 1) % 4
            current_direction = directions[idx]
            next_position = add_tuples(current, current_direction)

        current = next_position
        if current not in visited:
            visited.append(current)

    return visited


def solve_part1(fileInfo):
    (obstacles, start, width, height) = get_values(fileInfo)
    visited = move(obstacles, start, width, height)
    return len(visited)


def solve_part2(fileInfo):
    return 0