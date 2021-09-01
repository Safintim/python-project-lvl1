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


def run(user_name):
    engine.print_instruction(INSTRUCTION_TEXT)

    count_correct_answers = 0
    while not engine.is_win(count_correct_answers):
        question = make_question()
        engine.print_question(question.number)
        user_answer = engine.get_user_answer()
        if not engine.is_correct_answer(user_answer, question.answer):
            engine.print_wrong(user_answer, question.answer, user_name)
            break
        count_correct_answers += 1
        engine.print_correct()
    else:
        engine.print_congratulations(user_name)
