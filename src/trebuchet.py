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
