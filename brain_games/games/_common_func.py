from collections import namedtuple

from brain_games import engine


YES_TEXT = 'yes'
NO_TEXT = 'no'
Question = namedtuple(
    'Question',
    ('number', 'answer', 'to_str'),
)


def is_even(number):
    return number % 2 == 0


def make_question(predicate=is_even):
    number = engine.get_random_number()
    answer = YES_TEXT if predicate(number) else NO_TEXT
    return Question(number=number, answer=answer, to_str=number)
