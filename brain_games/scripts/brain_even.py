#!/usr/bin/env python3

brain-games

from brain_games.task import random_number

def condition(text):
  print(text)

def answer(text):
  print(text)

def main():
  condition('Answer "yes" if the number is even, otherwise answer "no".')
  random_number()

  answer('Your answer: ')

if __name__ == '__main__':
    main()
  
