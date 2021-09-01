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
    ('term1', 'term2', 'op', 'action', 'answer',),
)


def get_random_operation():
    op, action = random.choice(list(OPERATIONS.items()))
    return op, action


def make_question():
    term1 = engine.get_random_number()
    term2 = engine.get_random_number()
    op, action = get_random_operation()
    return Question(
        term1=term1,
        term2=term2,
        op=op,
        action=action,
        answer=action(term1, term2)
    )


def format_question(question):
    return '{0} {1} {2}'.format(question.term1, question.op, question.term2)


start_game = engine.make_game(
    instruction_text=INSTRUCTION_TEXT,
    make_question=make_question,
    format_question=format_question,
)
