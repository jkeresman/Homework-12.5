import json


def read_from_json(json_file):
    with open(json_file, "r") as score_file:
        score_list = json.loads(score_file.read())
    return score_list


def write_to_json(json_file, score_list):
    with open(json_file, "w") as score_file:
        score_file.write(json.dumps(score_list))
