import pytest

from src.day02 import solve_part1, solve_part2

day = "02"

@pytest.mark.parametrize("day", [day])
def test_part1(day, expected_value=2):
    testdata = {"key": "sample", "file": f"test/data/day{day}.sample.dat"}
    assert solve_part1(testdata) == expected_value

@pytest.mark.parametrize("day", [day])
def test_part2(day, expected_value=4):
    testdata = {"key": "sample", "file": f"test/data/day{day}.sample.dat"}
    assert solve_part2(testdata) == expected_value

@pytest.mark.parametrize("day", [day])
def test_part2_coverage(day, expected_value=3):
    testdata = {"key": "sample", "file": f"test/data/day{day}.sample-01.dat"}
    assert solve_part2(testdata) == expected_value
