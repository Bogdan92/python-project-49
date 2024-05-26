import prompt

import random

def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    print(f"{'Hello'}, {name}!")

def condition():
  print('What number is missing in the progression?')

def text():
  return 'Question:'

def end_game():
  print(f'Congratulations, {name}!')

def generate_progression():
  first_term = random.randint(1, 10)
  difference = random.randint(1, 5)
  length = random.randint(5, 10)
  progression = [str(first_term + i * difference) for i in range(length)]
  random_index = random.randint(0, length - 1)
  result = progression[random_index]
  progression[random_index] = '..'
  return ' '.join(progression), result

def user_answer():
  condition()
  for _ in range(3):  
    expression, result =  generate_progression()   
    print(text(), expression)
    answer = prompt.string('Your answer: ')
    if answer == str(result):
      print('Correct!')
    elif answer != str(result):
      print(f"{answer} is wrong answer ;(. Correct answer was {result}.\nLet's try again, {name}!")
      return
  end_game()
