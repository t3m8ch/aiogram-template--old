import random


class RandomNumbersService:
    def __init__(self, min_value: int = 0, max_value: int = 100):
        self._min_value = min_value
        self._max_value = max_value

    def generate_random_number(self) -> int:
        return random.randint(self._min_value, self._max_value)
