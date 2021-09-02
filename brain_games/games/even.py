import brain_games.games._common_func as common
from brain_games import engine


INSTRUCTION_TEXT = 'Answer "yes" if the number is even, otherwise answer "no".'


def start():
    return engine.run_game(
        instruction_text=INSTRUCTION_TEXT,
        make_question=common.make_question,
        is_int_answer=False,
    )
