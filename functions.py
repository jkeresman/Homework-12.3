
def want_to_play():
    answer = input("Want to play again? [yes/no]: ")
    return answer.lower() == "yes"


def calculate_score(correct_answers, number_of_questions):
    return correct_answers / number_of_questions * 100


def filter_by_level(score_list, level):
    return list(filter(lambda d: d["level"] == level, score_list))


def get_top_scores(score_list, level):
    scores = filter_by_level(score_list=score_list, level=level)
    sorted_scores = sorted(scores, key=lambda d: d["score"], reverse=True)
    return sorted_scores[:3]


def print_top_scores(score_list, level):
    print("Top scores: ")
    top_scores = get_top_scores(score_list=score_list, level=level)
    for i, player in enumerate(top_scores):
        print(f"{i + 1}. {player['first_name']} {player['last_name']}, attempts: {player['score']}")
