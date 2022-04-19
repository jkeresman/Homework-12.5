from files import *
from functions import *
import datetime
import random

score_json = "score.json"
score_list = read_from_json(json_file=score_json)

while want_to_play():

    secret = random.randint(1, 30)
    attempts = 0

    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    while True:
        level = input("Choose level [easy / hard]: ")
        try:
            level_check(level)
            break
        except NonExistingLevelException as ex:
            print(ex)

    while True:

        guess = guess_input_check()
        attempts += 1

        if guess == secret:
            score_list.append(
                {
                    "first_name": first_name,
                    "last_name": last_name,
                    "attempts": attempts,
                    "wrong_guesses": attempts - 1,
                    "date": str(datetime.datetime.now()),
                    "level": level,
                }
            )

            write_to_json(json_file=score_json, score_list=score_list)

            print("You've guessed it. It is number " + str(secret))
            print("Attempts needed " + str(attempts))

            while True:
                show_top_scores = input("Wanna see top players at your level [yes / no]: ")
                try:
                    yes_no_check(show_top_scores)
                    break
                except YesNoException as ex:
                    print(ex)

            if show_top_scores.lower() == "yes":
                print(f"TOP SCORES -> LEVEL = {level}")
                for i, player in enumerate(get_top_scores(score_list=score_list, level=level)):
                    print(f"{i + 1}. {player['first_name']} {player['last_name']}, attempts: {player['attempts']}")

            break

        elif level.lower() == "easy":
            get_hints(guess=guess, secret=secret)
