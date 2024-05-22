import prompt

import random

def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    print(f"{'Hello'}, {name}!")

def condition():
  print('Find the greatest common divisor of given numbers.')

def text():
  return 'Question:'

def end_game():
  print(f'Congratulations, {name}!')

def generate_expression():
  num1 = random.randint(1, 100)
  num2 = random.randint(1, 100)
  return (num1, num2)
 

def common_divisor(expression):  
  num1, num2 = expression
  while num1 != 0 and num2 != 0:
    if num1 > num2:
      num1 = num1 % num2
    else:
      num2 = num2 % num1
  return num1 + num2

def generate_expression_with_result():
  expression = generate_expression()
  result = common_divisor(expression)
  return expression, result

def user_answer():
  condition()
  for _ in range(3):  
    expression, result =  generate_expression_with_result()   
    print(text(), expression)
    answer = prompt.string('Your answer: ')
    if answer == str(result):
      print('Correct!')
    elif answer != str(result):
      print(f"{answer} is wrong answer ;(. Correct answer was {result}.\nLet's try again, {name}!")
      return
  end_game()
