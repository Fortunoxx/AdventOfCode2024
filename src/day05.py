def get_values(fileInfo):
    with open(fileInfo["file"], 'r') as file:
        a = [[int(l) for l in line.split('|')] for line in file if '|' in line]
    with open(fileInfo["file"], 'r') as file:
        b = [[int(l) for l in line.split(',')] for line in file if ',' in line]
    return (a, b)


def is_page_correct(rules, pages):
    indexed = {page: page_idx for page_idx, page in enumerate(pages)}
    for rule in rules:
        if rule[0] in indexed and rule[1] in indexed:
            if indexed[rule[0]] > indexed[rule[1]]:
                return False
    return True


def get_correct_pages(rules, page_list):
    correct = []
    for page in page_list:
        if is_page_correct(rules, page):
            correct.append(page)
    return correct


def solve_part1(fileInfo):
    rules, page_list = get_values(fileInfo)
    correct = get_correct_pages(rules, page_list)
    return sum([c[divmod(len(c), 2)[0]] for c in correct])


def solve_part2(fileInfo):
    return 0