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


def run(user_name):
    engine.print_instruction(INSTRUCTION_TEXT)

    count_correct_answers = 0
    while not engine.is_win(count_correct_answers):
        question = make_question()
        engine.print_question(
            '{0} {1}'.format(question.number1, question.number2),
        )
        user_answer = engine.get_user_answer(is_int=True)
        if not engine.is_correct_answer(user_answer, question.answer):
            engine.print_wrong(user_answer, question.answer, user_name)
            break
        count_correct_answers += 1
        engine.print_correct()
    else:
        engine.print_congratulations(user_name)
