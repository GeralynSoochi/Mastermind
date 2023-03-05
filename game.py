import random

def update_conf(no_tries, code_len):
    global colors
    global tries
    global code_length 

    colors = ["R", "G", "B", "Y", "W", "O"]
    tries = int(no_tries)
    code_length = int(code_len)

def generate_code():
    code = []

    for _ in range(code_length):
        color = random.choice(colors)
        code.append(color)

    return code

def guess_code():

    while True:
        sample_string = "R "*code_length
        guess = input(f"Guess (e.g.: {sample_string}): ").upper().split(" ")

        if len(guess) != code_length:
            print(f"You must guess {code_length} colors.")
            continue

        for color in guess:
            if color not in colors:
                print(f"nvalid color: {color}. Try again.")
        
        else:
            break
    
    return guess

def check_code(guess, real_code):
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1
            color_counts[guess_color] -= 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1

    return correct_pos, incorrect_pos

def game():
    print(f"Welcome to mastermind, you have {tries} tries to guess the code")
    print("The valid colors are", *colors)

    code = generate_code()
    for attempts in range(1, tries + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)

        if correct_pos == code_length:
            print(f"You guessed the code in {attempts} tries!")
            break

        print(f"Correct Positions: {correct_pos} | Incorrect Positions: {incorrect_pos}")

    else:
        print("You ran out of tries, the code was:", *code)


def check_numeric(conf_type):
    num_conf = input(f"Input max {conf_type}: ")
    while not num_conf.isnumeric():
        print("You did not enter a number. Please try again.")
        num_conf = input(f"Input max {conf_type}: ")

    return num_conf

def config():
    tries = 10
    code_len = 4
    config = input("Edit configs for tries and code length (Y/N)? ").upper()
    if config == "Y":
        tries = check_numeric("tries")
        code_len = check_numeric("code length")

        #colors = ["R", "G", "B", "Y", "W", "O"]
    update_conf(tries, code_len)

if __name__ == "__main__":
    while True:
        start = input("Start a new game (Y/N)? ").upper()
        if start == "Y":
            config()
            game()
        else: 
            break