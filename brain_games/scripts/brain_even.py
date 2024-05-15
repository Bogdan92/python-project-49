#!/usr/bin/env python3

from brain_games.cli import welcome_user

from brain_games.task import user_answer

from brain_games.cli import name

global name

def main():
  welcome_user()
  user_answer()


if __name__ == '__main__':
    main()
