def get_values(fileInfo):
    file = open(fileInfo["file"]).readlines()
    return [[int(item) for item in line.split()] for line in file]


def calc(items, max_diff=3, min_diff=1):
    counter = 0

    for record in items:
        previous = None
        direction = None
        
        for i in record:
            fault = False
    
            if previous is None:
                previous = i
                continue
            else:
                if previous == i:
                    fault = True
                    break
                if previous < i:
                    if direction is None:
                        direction = "up"
                    elif direction is not "up":
                        fault = True
                        break
                    if(i - previous > max_diff or i - previous < min_diff):
                        fault = True
                        break
                else:
                    if direction is None:
                        direction = "down"
                    elif direction is not "down":
                        fault = True
                        break
                    if(previous - i > max_diff or previous - i < min_diff):
                        fault = True
                        break

                previous = i
    
        if not fault:
            counter += 1

    return counter


def solve_part1(fileInfo):
    items = get_values(fileInfo)
    return calc(items)


def solve_part2(fileInfo):
    return 0