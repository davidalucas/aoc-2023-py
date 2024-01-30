from src.trebuchet import sum_all_cal_values, parse_cal_value


def test_parse_cal_value_returns_expected():
    assert parse_cal_value("1abc2") == 12
    assert parse_cal_value("pqr3stu8vwx") == 38
    assert parse_cal_value("a1b2c3d4e5f") == 15
    assert parse_cal_value("treb7uchet") == 77


def test_sum_all_cal_values_works_with_example_data():
    assert sum_all_cal_values("data/day_1/example_1.txt") == 142


def test_sum_all_cal_values_works_with_real_data():
    assert sum_all_cal_values("data/day_1/data.txt") == 55477
