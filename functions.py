from level_exception import NonExistingLevelException
from yes_no_exception import YesNoException


def get_top_scores(score_list, level):
    filtered_by_level = list(filter(lambda p: p["level"] == level, score_list))
    sorted_score_list = sorted(filtered_by_level, key=lambda d: d["attempts"])
    return sorted_score_list[:3]


def get_hints(guess, secret):
    if guess > secret:
        print("Wrong guess. Try something smaller!!")
    elif guess < secret:
        print("Wrong guess. Try something bigger!!")


def want_to_play():
    while True:
        answer = input("Do you want play secret number game[yes/no]")
        try:
            yes_no_check(answer)
            break
        except YesNoException as ex:
            print(ex)

    return answer.lower() == "yes"


def guess_input_check():
    while True:
        try:
            guess = int(input("Guess the secret number between 1 and 30: "))
            break
        except ValueError:
            print("Wrong input, please try again!!!")
    return guess


def level_check(level):
    level_lowercase = level.lower()
    if level_lowercase != "hard" and level_lowercase != "easy":
        raise NonExistingLevelException(f"Level: {level} does not exsist")


def yes_no_check(answer):
    answer_lowercase = answer.lower()
    if answer_lowercase != "yes" and answer_lowercase != "no":
        raise YesNoException(f"{answer} is neither yes or no")