from collections import namedtuple

from brain_games import engine


INSTRUCTION_TEXT = '"yes" if given number is prime. Otherwise answer "no".'
YES_TEXT = 'yes'
NO_TEXT = 'no'
Question = namedtuple(
    'Question',
    ('number', 'answer',),
)


def is_prime(number):
    if number % 2 == 0:
        return number == 2

    div = 3
    while div * div < number and number % div != 0:
        div += 3

    return div * div > number


def make_question():
    number = engine.get_random_number()
    answer = YES_TEXT if is_prime(number) else NO_TEXT
    return Question(number=number, answer=answer)


def run(user_name):
    engine.print_instruction(INSTRUCTION_TEXT)

    count_correct_answers = 0
    while not engine.is_win(count_correct_answers):
        question = make_question()
        engine.print_question(question.number)
        user_answer = engine.get_user_answer(is_int=True)
        if not engine.is_correct_answer(user_answer, question.answer):
            engine.print_wrong(user_answer, question.answer, user_name)
            break
        count_correct_answers += 1
        engine.print_correct()
    else:
        engine.print_congratulations(user_name)
