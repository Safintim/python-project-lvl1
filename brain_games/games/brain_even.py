from collections import namedtuple

from brain_games import engine


INSTRUCTION_TEXT = 'Answer "yes" if the number is even, otherwise answer "no".'
YES_TEXT = 'yes'
NO_TEXT = 'no'
Question = namedtuple(
    'Question',
    ('number', 'answer',),
)


def make_question():
    number = engine.get_random_number()
    answer = YES_TEXT if is_even(number) else NO_TEXT
    return Question(number=number, answer=answer)


def is_even(number):
    return number % 2 == 0


def format_question(question):
    return question.number


start_game = engine.make_game(
    instruction_text=INSTRUCTION_TEXT,
    make_question=make_question,
    format_question=format_question,
    is_int_answer=False,
)
