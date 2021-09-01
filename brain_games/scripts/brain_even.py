#!/usr/bin/env python
from brain_games import cli, brain_even


def main():
    print('Welcome to the Brain Games!')
    user_name = cli.welcome_user()
    brain_even.run(user_name)


if __name__ == '__main__':
    main()
