import random
import prompt


CORRECT_ANSWER_TEXT = 'Correct!'
USER_ANSWER_TEXT = 'Your answer: '
WRONG_ANSWER_PATTERN = ''''{0}' is wrong answer ;(. Correct answer was '{1}'.
Let's try again, {2}!'''
QUESTION_PATTERN = 'Question: {0}'
CONGRATULATION_PATTERN = 'Congratulations, {0}!'
COUNT_CORRECT_ANSWERS = 3
RANGE_NUMBERS = (1, 100)


def is_win(count_correct_answers):
    return count_correct_answers == COUNT_CORRECT_ANSWERS


def print_instruction(instruction):
    print(instruction)


def print_question(pattern):
    print(QUESTION_PATTERN.format(pattern))


def print_wrong(user_answer, correct_answer, user_name):
    print(WRONG_ANSWER_PATTERN.format(user_answer, correct_answer, user_name))


def print_correct():
    print(CORRECT_ANSWER_TEXT)


def print_congratulations(user_name):
    print(CONGRATULATION_PATTERN.format(user_name))


def get_user_answer(is_int=False):
    answer = prompt.string(USER_ANSWER_TEXT)

    if is_int:
        try:
            answer = int(answer)
        except ValueError:
            pass
    return answer


def get_random_number(range_numbers=RANGE_NUMBERS):
    return random.randint(*range_numbers)
