from src.trebuchet import parse_cal_value


def test_parse_cal_value_returns_expected():
    assert parse_cal_value("1abc2") == 12
    assert parse_cal_value("pqr3stu8vwx") == 38
    assert parse_cal_value("a1b2c3d4e5f") == 15
    assert parse_cal_value("treb7uchet") == 77
