from src.cube_game import CubeGame
from assertpy import assert_that


def test_from_string_constructs_correctly():
    expected = CubeGame(
        1, [{"red": 4, "blue": 3}, {"red": 1, "green": 2, "blue": 6}, {"green": 2}]
    )
    actual = CubeGame.from_string(
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    )

    assert actual.id == expected.id
    assert actual.reveals == expected.reveals
