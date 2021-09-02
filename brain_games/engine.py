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


def is_correct_answer(user_answer, correct_answer):
    return user_answer == correct_answer


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


def get_user_answer(is_int=True):
    answer = prompt.string(USER_ANSWER_TEXT)

    if is_int:
        try:
            answer = int(answer)
        except ValueError:
            pass
    return answer


def get_random_number(range_numbers=RANGE_NUMBERS):
    return random.randint(*range_numbers)


def get_user_name():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    return name


def run_game(instruction_text, make_question, is_int_answer=True):
    user_name = get_user_name()
    print_instruction(instruction_text)

    count_correct_answers = 0
    while not is_win(count_correct_answers):
        question = make_question()
        print_question(question.to_str)
        user_answer = get_user_answer(is_int_answer)
        if not is_correct_answer(user_answer, question.answer):
            print_wrong(user_answer, question.answer, user_name)
            break
        count_correct_answers += 1
        print_correct()
    else:
        print_congratulations(user_name)
