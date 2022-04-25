from files_functions import *
from functions import *
import constants


def play_game(country_dict, level):

    score_file = "score.json"

    score_list = read_from_json(score_file)

    print_top_scores(score_list=score_list, level=level)

    correct_answers = 0
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    for country, capital_city in country_dict.items():
        print(f"What is capital city of {country}?")
        answer = input("Your answer: ")
        if answer.lower() == capital_city.lower():
            print("Correct!!!!")
            correct_answers += 1
        else:
            print(f"Wrong, right answer is {capital_city}")

    score = calculate_score(correct_answers=correct_answers, number_of_questions=len(country_dict))

    score_list.append(
        {
            "first_name": first_name,
            "last_name": last_name,
            "score": score,
            "level": level,
        }
    )

    write_to_json(json_file=score_file, score_list=score_list)

    print("Your score: {:.2f} %".format(score))


def main():

    play_again = True

    while play_again:

        level = input("Choose level [easy / medium / hard]: ")

        if level.lower() == "easy":
            play_game(country_dict=constants.EASY_COUNTRIES, level=level)
        elif level.lower() == "medium":
            play_game(country_dict=constants.MEDIUM_COUNTRIES, level=level)
        elif level.lower() == "hard":
            play_game(country_dict=constants.HARD_COUNTRIES, level=level)

        play_again = want_to_play()


if __name__ == "__main__":
    main()
