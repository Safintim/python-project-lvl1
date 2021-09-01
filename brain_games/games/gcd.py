import math

from collections import namedtuple

from brain_games import engine


INSTRUCTION_TEXT = 'Find the greatest common divisor of given numbers.'
Question = namedtuple(
    'Question',
    ('number1', 'number2', 'answer',),
)


def make_question():
    number1 = engine.get_random_number()
    number2 = engine.get_random_number()
    answer = math.gcd(number1, number2)
    return Question(number1=number1, number2=number2, answer=answer)


def format_question(question):
    return '{0} {1}'.format(question.number1, question.number2)


start_game = engine.make_game(
    instruction_text=INSTRUCTION_TEXT,
    make_question=make_question,
    format_question=format_question,
)
