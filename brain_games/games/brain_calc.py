import operator
import random
from collections import namedtuple

from brain_games import engine


INSTRUCTION_TEXT = 'What is the result of the expression?'
OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}
Question = namedtuple(
    'Question',
    ('term1', 'term2', 'op', 'action'),
)


def get_random_operation():
    op, action = random.choice(list(OPERATIONS.items()))
    return op, action


def get_correct_answer(operand1, operand2, action):
    return action(operand1, operand2)


def make_question():
    op, action = get_random_operation()
    return Question(
        term1=engine.get_random_number(),
        term2=engine.get_random_number(),
        op=op,
        action=action,
    )


def run(user_name):
    engine.print_instruction(INSTRUCTION_TEXT)

    count_correct_answers = 0
    while not engine.is_win(count_correct_answers):
        question = make_question()
        engine.print_question(
            '{0} {1} {2}'.format(question.term1, question.op, question.term2),
        )
        user_answer = engine.get_user_answer(is_int=True)
        correct_answer = get_correct_answer(
            question.term1, question.term2, question.action,
        )
        if not engine.is_correct_answer(user_answer, correct_answer):
            engine.print_wrong(user_answer, correct_answer, user_name)
            break
        count_correct_answers += 1
        engine.print_correct()
    else:
        engine.print_congratulations(user_name)
