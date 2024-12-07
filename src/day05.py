def get_values(fileInfo):
    with open(fileInfo["file"], "r") as file:
        a = [[int(l) for l in line.split("|")] for line in file if "|" in line]
    with open(fileInfo["file"], "r") as file:
        b = [[int(l) for l in line.split(",")] for line in file if "," in line]
    return (a, b)


def is_page_correct(rules, pages):
    indexed = {page: page_idx for page_idx, page in enumerate(pages)}
    for rule in rules:
        if rule[0] in indexed and rule[1] in indexed:
            if indexed[rule[0]] > indexed[rule[1]]:
                return False
    return True


def get_correct_pages(rules, page_list, find_correct=True):
    correct = []
    for page in page_list:
        if is_page_correct(rules, page) is find_correct:
            correct.append(page)
    return correct


def order_rules(rules, incorrect):
    val = []
    for pages in incorrect:
        results = []
        while len(results) < len(pages):
            results.append(find_rule_without_parent(rules, pages, results))
        val.append([orc for orc in results if orc in pages])
    return val


def find_rule_without_parent(rules, distinct_values=[], exceptions=[]):
    dvc = [d for d in distinct_values if d not in exceptions]
    filtered_rules = [rule for rule in rules if (rule[0] not in exceptions and rule[0] in dvc and rule[1] in dvc)]
    # find the one that has no predecessor
    for value in distinct_values:
        for rule in filtered_rules:
            if rule[1] == value:
                dvc.remove(value)
                break        
    return dvc[0]


def solve_part1(fileInfo):
    rules, page_list = get_values(fileInfo)
    correct = get_correct_pages(rules, page_list)
    return sum([c[divmod(len(c), 2)[0]] for c in correct])


def solve_part2(fileInfo):
    rules, page_list = get_values(fileInfo)
    incorrect = get_correct_pages(rules, page_list, False)
    ordered_pages = order_rules(rules, incorrect)
    return sum([c[divmod(len(c), 2)[0]] for c in ordered_pages])
