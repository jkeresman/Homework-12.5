
class NonExistingLevelException(Exception):
    def __init__(self, wrong_input):
        self.wrong_input = wrong_input

    def __repr__(self):
        return f"{self.wrong_input} is neither EASY or HARD !!!"


class YesNoException(Exception):
    def __init__(self, wrong_input):
        self.wrong_input = wrong_input

    def __repr__(self):
        return f"{self.wrong_input} is neither YES or NO !!!"
