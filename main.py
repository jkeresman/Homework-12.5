from functions import *
from json_functions import read_from_json, write_to_json
import datetime
import random

from player import Player


def main():

    score_json = "json_files/score.json"
    score_list = read_from_json(json_file=score_json)

    while want_to_play():

        secret = random.randint(1, 30)
        attempts = 0

        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        full_name = first_name + " " + last_name
        level = level_input()

        while True:

            guess = guess_input_check()
            attempts += 1

            if guess == secret:
                player = Player(
                    full_name=full_name,
                    score=attempts,
                    level=level,
                    date=str(datetime.datetime.now())
                )
                score_list.append(player.__dict__)

                print("You've guessed it. It is number " + str(secret))
                print("Attempts needed " + str(attempts))

                show_top_scores = show_scores_input()

                if show_top_scores.lower() == "yes":

                    print(f"TOP SCORES -> LEVEL = {level}")
                    top_scores = get_top_scores(score_list=score_list, level=level)

                    for i, player in enumerate(top_scores):
                        print(f"{i + 1}. {player}")

                break

            elif level.lower() == "easy":
                get_hints(guess=guess, secret=secret)

        write_to_json(json_file=score_json, score_list=score_list)


if __name__ == "__main__":
    main()
