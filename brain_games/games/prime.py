import brain_games.games._common_func as common
from brain_games import engine


INSTRUCTION_TEXT = '"yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if common.is_even(number):
        return number == 2

    if number < 2:
        return False

    div = 3
    while div * div < number and number % div != 0:
        div += 2

    return div * div > number


def start():
    return engine.run_game(
        instruction_text=INSTRUCTION_TEXT,
        make_question=lambda: common.make_question(predicate=is_prime),
    )
