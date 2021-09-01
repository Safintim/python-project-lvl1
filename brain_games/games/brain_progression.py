from collections import namedtuple
import random

from brain_games import engine


INSTRUCTION_TEXT = 'What number is missing in the progression?'
RANGE_PROGRESSION_STEP = (1, 10)
PROGRESSION_SIZE = 10
Question = namedtuple(
    'Question',
    ('progression', 'answer',),
)


def make_progression():
    start = engine.get_random_number()
    step = engine.get_random_number(range_numbers=RANGE_PROGRESSION_STEP)
    end = start + (step * PROGRESSION_SIZE)
    return list(range(start, end, step))


def make_question():
    progression = make_progression()
    missing_index = random.choice(range(PROGRESSION_SIZE))
    answer = progression[missing_index]
    progression[missing_index] = '..'
    progression = ' '.join(str(item) for item in progression)
    return Question(progression=progression, answer=answer)


def run(user_name):
    engine.print_instruction(INSTRUCTION_TEXT)

    count_correct_answers = 0
    while not engine.is_win(count_correct_answers):
        question = make_question()
        engine.print_question(question.progression)
        user_answer = engine.get_user_answer(is_int=True)
        if not engine.is_correct_answer(user_answer, question.answer):
            engine.print_wrong(user_answer, question.answer, user_name)
            break
        count_correct_answers += 1
        engine.print_correct()
    else:
        engine.print_congratulations(user_name)
