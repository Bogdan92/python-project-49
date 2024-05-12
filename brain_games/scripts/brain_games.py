#!/usr/bin/env python3


from brain_games.cli import welcome_user
from brain_games.cli import name


welcome_user(name)


def greet(text):
    print(text)


def main():
    greet('Welcome to the Brain Games!')


if __name__ == '__main__':
    main()
