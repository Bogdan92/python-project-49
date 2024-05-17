import prompt

import random

def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    print(f"{'Hello'}, {name}!")

def condition():
  print('What is the result of the expression?')

def text():
  return 'Question:'

def end_game():
  print(f'Congratulations, {name}!')

def generate_expression():
  num1 = random.randint(1, 10)
  num2 = random.randint(1, 10)
  operator = random.choice(['+', '-', '*'])
  expression = f"{num1} {operator} {num2}"
  return expression
    
def generate_expression_with_result():
  expression = generate_expression()
  result = eval(expression)
  return expression, result

def user_answer():
  condition()
  for _ in range(3):  
    expression, result = generate_expression_with_result()
    print(text(), expression)
    answer = prompt.string('Your answer: ')
    if answer == str(result):
      print('Correct!')
    elif answer != str(result):
      print(f"{answer} is wrong answer ;(. Correct answer was {result}.\nLet's try again, {name}!")
      return
  end_game()
