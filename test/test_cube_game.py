from src.cube_game import CubeGame, sum_game_powers, sum_possible_games
from assertpy import assert_that


def test_cubegame_constructor():
    id: int = 1
    reveals = [{"red": 4, "blue": 3}, {"red": 1, "green": 2, "blue": 6}, {"green": 2}]
    min_colors = {"red": 4, "green": 2, "blue": 6}

    game = CubeGame(
        1, [{"red": 4, "blue": 3}, {"red": 1, "green": 2, "blue": 6}, {"green": 2}]
    )
    assert_that(game.id).is_equal_to(id)
    assert_that(game.reveals).is_equal_to(reveals)
    assert_that(game.min_colors).is_equal_to(min_colors)


def test_from_string_constructs_correctly():
    expected = CubeGame(
        1, [{"red": 4, "blue": 3}, {"red": 1, "green": 2, "blue": 6}, {"green": 2}]
    )
    actual = CubeGame.from_string(
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    )

    assert actual.id == expected.id
    assert actual.reveals == expected.reveals


def test_is_valid_returns_false_when_expected():
    cube_game = CubeGame.from_string(
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
    )

    valid_dict = {"red": 12, "green": 13, "blue": 14}

    assert_that(cube_game.is_valid(valid_dict)).is_false()


def test_is_valid_returns_true_when_expected():
    cube_game = CubeGame.from_string(
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"
    )

    valid_dict = {"red": 12, "green": 13, "blue": 14}

    assert_that(cube_game.is_valid(valid_dict)).is_true()


def test_sum_possible_games_works_for_example_data():
    limits = {"red": 12, "green": 13, "blue": 14}
    actual = sum_possible_games("data/day_2/example.txt", limits)
    assert_that(actual).is_equal_to(8)


def test_sum_possible_games_works_for_real_data():
    limits = {"red": 12, "green": 13, "blue": 14}
    actual = sum_possible_games("data/day_2/data.txt", limits)
    assert_that(actual).is_equal_to(2727)


def test_sum_game_powers_works_for_example_data():
    actual = sum_game_powers("data/day_2/example.txt")
    assert_that(actual).is_equal_to(2286)


def test_sum_game_powers_works_for_real_data():
    actual = sum_game_powers("data/day_2/data.txt")
    assert_that(actual).is_equal_to(56580)
