from typing import List


class CubeGame:
    def __init__(self, id: int, reveals: List[dict[str, int]]):
        self.id = id
        self.reveals = reveals

    @staticmethod
    def from_string(data: str):
        """
        Converts a string representation of a CubeGame object into an actual CubeGame object.

        Args:
            data (str): The string representation of the CubeGame object.

        Returns:
            CubeGame: The CubeGame object created from the string representation.
        """
        game_split = data.split(": ")
        game_id = int(game_split[0].split(" ")[1])

        reveals: List[dict[str, int]] = []
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
