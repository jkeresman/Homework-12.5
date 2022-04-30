
class Player:

    def __init__(self, full_name: str, score: int, level: str, date: str):
        self.full_name = full_name
        self.score = score
        self.level = level
        self.date = date

    def __repr__(self):
        return f"{self.__class__.__name__} -> {self.full_name}, score: {self.score}, date: {self.date}"
