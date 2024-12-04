import requests
import os

year = 2024
cookiePath = "src/puzzle/cookie.txt"
text = "Please don't repeatedly request this endpoint before it unlocks! The calendar countdown is synchronized with the server time; the link will be enabled on the calendar the instant this puzzle becomes available.\n"

def fetch_for_day(day):
        filename = f"src/data/day{day}.input.dat"
        needs_reload = False

        if os.path.exists(filename):
            with open(filename, "r") as file:
                if file.readline() == text:
                    needs_reload = True

        if not os.path.exists(filename) or needs_reload:
            save_to_file(get_input(year, day), filename)
            return (filename, False)
        return (filename, True)


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