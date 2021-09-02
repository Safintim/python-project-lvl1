from collections import namedtuple
import random

from brain_games import engine


INSTRUCTION_TEXT = 'What number is missing in the progression?'
RANGE_PROGRESSION_STEP = (1, 10)
PROGRESSION_SIZE = 10
Question = namedtuple(
    'Question',
    ('progression', 'answer', 'to_str'),
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
    return Question(progression=progression, answer=answer, to_str=progression)


def start():
    return engine.run_game(
        instruction_text=INSTRUCTION_TEXT,
        make_question=make_question,
    )
