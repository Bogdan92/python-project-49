#!/usr/bin/env python3


from brain_games.cli import welcome_user
from brain_games.cli import name


def greet(text):
    print(text)
    

welcome_user(name)


def main():
    greet('Welcome to the Brain Games!')


if __name__ == '__main__':
    main()
