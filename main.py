import datetime
import json
import random

secret = random.randint(1, 30)
attempts = 0

with open("score.json", "r") as score_file:
    score_list = json.loads(score_file.read())

sorted_score_list = sorted(score_list, key=lambda d: d["attempts"])

print("TOP SCORES: ")
for i, player in enumerate(sorted_score_list[0:3]):
    print(f"{i + 1}. {player['first_name']} {player['last_name']}, attempts: {player['attempts']}")

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

while True:
    guess = int(input("Guess the secret number between 1 and 30: "))
    attempts += 1

    if guess == secret:
        score_list.append(
            {
                "first_name": first_name,
                "last_name": last_name,
                "attempts": attempts,
                "wrong_guesses": attempts - 1,
                "date": str(datetime.datetime.now())
            }
        )

        with open("score.json", "w") as score_file:
            score_file.write(json.dumps(score_list))

        print("You've guessed it. It is number " + str(secret))
        print("Attempts needed " + str(attempts))
        break

    elif guess > secret:
        print("Wrong guess. Try something smaller!!")

    elif guess < secret:
        print("Wrong guess. Try something bigger!!")
