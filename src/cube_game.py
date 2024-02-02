class CubeGame:
    def __init__(self, id: int, reveals: list[dict[str, int]]):
        self.id = id
        self.reveals = reveals

        self.min_colors: dict[str, int] = {"red": 0, "green": 0, "blue": 0}

        for reveal in reveals:
            for key, val in reveal.items():
                if self.min_colors[key] < val:
                    self.min_colors[key] = val

    @staticmethod
    def from_string(data: str) -> "CubeGame":
        """
        Converts a string representation of a CubeGame object into an actual CubeGame object.

        Args:
            data (str): The string representation of the CubeGame object.

        Returns:
            CubeGame: The CubeGame object created from the string representation.
        """
        game_split = data.split(": ")
        game_id = int(game_split[0].split(" ")[1])

        reveals: list[dict[str, int]] = []
        for reveals_raw_data in game_split[1].split("; "):
            reveal: dict[str, int] = {}
            for reveal_str in reveals_raw_data.split(", "):
                [val_str, key] = reveal_str.split(" ")
                reveal[key] = int(val_str)
            reveals.append(reveal)

        return CubeGame(game_id, reveals)

    def is_valid(self, limits: dict[str, int]) -> bool:
        """
        Checks if the the game was actually possible based on the given RGB limits.

        Args:
            limits (dict[str, int]): A dictionary containing the RGB cube limits.

        Returns:
            bool: True if the game was possible, False otherwise.
        """
        for reveal in self.reveals:
            for key, val in reveal.items():
                if limits[key] < val:
                    return False
        return True


def sum_possible_games(path: str, limits: dict[str, int]) -> int:
    """
    Calculates the sum of valid game IDs based on the given path and limits.

    Args:
        path (str): The path to the file containing game data.
        limits (dict[str, int]): The limits for validating games.

    Returns:
        int: The sum of valid game IDs.
    """
    sum = 0
    with open(path, "r") as file:
        for line in file:
            line = line.rstrip("\n")
            game = CubeGame.from_string(line)
            if game.is_valid(limits):
                sum += game.id

    return sum
