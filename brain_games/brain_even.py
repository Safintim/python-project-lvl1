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


def is_even(number):
    return number % 2 == 0


def get_correct_answer(number):
    return YES_TEXT if is_even(number) else NO_TEXT


def run(user_name):
    print(INSTRUCTION_TEXT)

    count_correct_answers = 0
    while True:
        number = get_random_number()
        print(QUESTION_PATTERN.format(number))

        user_answer = prompt.string(USER_ANSWER_TEXT)
        correct_answer = get_correct_answer(number)

        if user_answer not in VALID_ANSWERS or user_answer != correct_answer:
            print(WRONG_ANSWER_PATTERN.format(
                user_answer, correct_answer, user_name))
            return

        count_correct_answers += 1
        print(CORRECT_ANSWER_TEXT)

        if count_correct_answers == COUNT_CORRECT_ANSWERS:
            print(CONGRATULATION_PATTERN.format(user_name))
            return
