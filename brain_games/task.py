import prompt

import random

def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    print(f"{'Hello'}, {name}!")

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
    result = random_number()
    print(text(), result)
    answer = prompt.string('Your answer: ')
    if (answer == 'yes' and result % 2 == 0) or (answer == 'no' and result % 2 != 0):
      print('Correct!')
    else:
        correct_answer = 'no' if answer == 'yes' else 'yes'
        print(f"'{answer}' is the wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {name}!")
        return
  end_game()
