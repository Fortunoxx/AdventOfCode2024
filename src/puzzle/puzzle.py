import requests
import os

year = 2024
cookiePath = "src/puzzle/cookie.txt"
text = "Please don't repeatedly request this endpoint before it unlocks!"

def fetch_for_day(day, locked = False):
    filename = f"src/data/day{day}.input.dat"
    needs_reload = False

    if os.path.exists(filename) and not locked:
        with open(filename, "r") as file:
            if file.readline().startswith(text):
                needs_reload = True

    if (not os.path.exists(filename) or needs_reload) and not locked:
        txt = get_input(year, day)
        save_to_file(txt, filename)
        return (filename, False, needs_reload)

    return (filename, True, locked)


def get_input(year, day):
    with open(cookiePath) as cookieFile:
        cookies = dict(session=cookieFile.readline())
        result = requests.get(
            f"https://adventofcode.com/{year}/day/{int(day)}/input",
            cookies=cookies,
        )
    return result.text


def save_to_file(text, filename):
    with open(filename, "w") as inputFile:
        inputFile.write(text)
    return filename