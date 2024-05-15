import prompt

import random

from brain_games.cli import welcome_user

from brain_games.cli import name

def condition():
  print('Answer "yes" if the number is even, otherwise answer "no".')

def text():
  return 'Question:'

def end_game():
  print(f'Congratulations, {name}!')

def random_number():
  return random.randint(1, 20)

def user_answer():
  condition()
  for i in range(3):
    global name
    result = random_number()
    print(text(), result)
    answer = prompt.string('Your answer: ')
    if answer == 'yes' and result % 2 == 0:
      print('Correct!')
    elif answer == 'no' and result % 2 != 0:
      print('Correct!')
    elif answer == 'yes' and result % 2 != 0:
      print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!")
      return
    elif answer == 'no' and result % 2 == 0:
      print(f"'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {name}!")
      return
    else:
      print(f"'{answer}' is wrong input. Please, use 'yes' or 'no'")
      return
  end_game()
