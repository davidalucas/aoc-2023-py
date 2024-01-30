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


def sum_all_cal_values(path: str) -> int:
    sum = 0
    with open(path, "r") as file:
        for line in file:
            sum += parse_cal_value(line)

    return sum
