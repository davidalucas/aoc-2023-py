nums: dict[str, int] = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def parse_cal_value(data: str) -> int:
    first: int = 0
    second: int = 0

    for ch in data:
        if ch.isdigit():
            first = int(ch)
            break

    for ch in reversed(data):
        if ch.isdigit():
            second = int(ch)
            break

    return first * 10 + second


def parse_cal_value_improved(data: str) -> int:
    first: int = 0
    second: int = 0

    for i, ch in enumerate(data):
        if ch.isdigit():
            first = int(ch)
            break
        found = False
        for key, val in nums.items():
            if i + len(key) > len(data):
                continue
            if data[i : i + len(key)] == key:
                first = val
                found = True
                break
        if found:
            break

    reversed_data: str = data[::-1]
    for i, ch in enumerate(reversed_data):
        if ch.isdigit():
            second = int(ch)
            break
        found = False
        for key, val in nums.items():
            if i + len(key) > len(reversed_data):
                continue
            if reversed_data[i : i + len(key)] == key[::-1]:
                second = val
                found = True
                break
        if found:
            break

    return first * 10 + second


def sum_all_cal_values(path: str) -> int:
    sum = 0
    with open(path, "r") as file:
        for line in file:
            sum += parse_cal_value(line)

    return sum
