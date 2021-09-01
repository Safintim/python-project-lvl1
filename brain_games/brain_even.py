import random
import prompt


INSTRUCTION_TEXT = 'Answer "yes" if the number is even, otherwise answer "no".'
CORRECT_ANSWER_TEXT = 'Correct!'
USER_ANSWER_TEXT = 'Your answer: '
YES_TEXT = 'yes'
NO_TEXT = 'no'
WRONG_ANSWER_PATTERN = ''''{0}' is wrong answer ;(. Correct answer was '{1}'.
Let's try again, {2}!'''
QUESTION_PATTERN = 'Question: {0}'
CONGRATULATION_PATTERN = 'Congratulations, {0}!'
VALID_ANSWERS = (YES_TEXT, NO_TEXT)
RANGE_NUMBERS = (1, 100)
COUNT_CORRECT_ANSWERS = 3


def get_random_number(range_numbers=RANGE_NUMBERS):
    return random.randint(*range_numbers)


def get_correct_answer(number):
    return YES_TEXT if is_even(number) else NO_TEXT


def get_user_answer():
    return prompt.string(USER_ANSWER_TEXT)


def is_even(number):
    return number % 2 == 0


def is_valid_answer(user_answer):
    return user_answer in VALID_ANSWERS


def is_correct_answer(user_answer, correct_answer):
    return user_answer == correct_answer


def is_ok_answer(user_answer, correct_answer):
    checks = (
        is_valid_answer(user_answer),
        is_correct_answer(user_answer, correct_answer),
    )
    return all(checks)


def is_win(count_correct_answers):
    return count_correct_answers == COUNT_CORRECT_ANSWERS


def print_instruction():
    print(INSTRUCTION_TEXT)


def print_question(number):
    print(QUESTION_PATTERN.format(number))


def print_wrong(user_answer, correct_answer, user_name):
    print(WRONG_ANSWER_PATTERN.format(user_answer, correct_answer, user_name))


def print_correct():
    print(CORRECT_ANSWER_TEXT)


def print_congratulations(user_name):
    print(CONGRATULATION_PATTERN.format(user_name))


def run(user_name):
    print_instruction()

    count_correct_answers = 0
    while not is_win(count_correct_answers):
        number = get_random_number()
        print_question(number)
        user_answer = get_user_answer()
        correct_answer = get_correct_answer(number)
        if not is_ok_answer(user_answer, correct_answer):
            print_wrong(user_answer, correct_answer, user_name)
            break
        count_correct_answers += 1
        print_correct()
    else:
        print_congratulations(user_name)
