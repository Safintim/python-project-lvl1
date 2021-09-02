import math

from collections import namedtuple

from brain_games import engine


INSTRUCTION_TEXT = 'Find the greatest common divisor of given numbers.'
Question = namedtuple(
    'Question',
    ('number1', 'number2', 'answer', 'to_str'),
)


def make_question():
    number1 = engine.get_random_number()
    number2 = engine.get_random_number()
    answer = math.gcd(number1, number2)
    return Question(
        number1=number1,
        number2=number2,
        answer=answer,
        to_str='{0} {1}'.format(number1, number2)
    )


def start():
    return engine.run_game(
        instruction_text=INSTRUCTION_TEXT,
        make_question=make_question,
    )
