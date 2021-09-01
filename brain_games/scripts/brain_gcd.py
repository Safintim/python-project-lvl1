#!/usr/bin/env python
from brain_games import cli
from brain_games.games import brain_gcd


def main():
    print('Welcome to the Brain Games!')
    user_name = cli.welcome_user()
    brain_gcd.run(user_name)


if __name__ == '__main__':
    main()
