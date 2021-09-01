#!/usr/bin/env python
from brain_games import cli
from brain_games.games.progression import start_game


def main():
    start_game(cli.get_user_name())


if __name__ == '__main__':
    main()
