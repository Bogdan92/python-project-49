import prompt

def welcome_user(name):
    print(name)

def main():
    name = prompt.string('May I have your name? ')
    welcome_user(name)

if __name__ == '__main__':
    main()
