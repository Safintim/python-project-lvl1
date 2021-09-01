from collections import namedtuple

from brain_games import engine


INSTRUCTION_TEXT = '"yes" if given number is prime. Otherwise answer "no".'
YES_TEXT = 'yes'
NO_TEXT = 'no'
Question = namedtuple(
    'Question',
    ('number', 'answer',),
)


def is_prime(number):
    if number % 2 == 0:
        return number == 2

    div = 3
    while div * div < number and number % div != 0:
        div += 3

    return div * div > number


def make_question():
    number = engine.get_random_number()
    answer = YES_TEXT if is_prime(number) else NO_TEXT
    return Question(number=number, answer=answer)


def format_question(question):
    return question.number


start_game = engine.make_game(
    instruction_text=INSTRUCTION_TEXT,
    make_question=make_question,
    format_question=format_question,
)
