import prompt
name = input()

def welcome_user(name):
    name = prompt.string('May I have your name? ')
    print(f"{'Hello'}, {name}!")
