import random

TRIES_LIMIT = 6
WORD_OPTIONS = ["NEW ZELAND", "NORTH KOREA", "SOUTH KOREA", "BRAZIL", "IRELAND", "RUSSIA", "SPAIN", "CANADA", "FRANCE", "ITALY", "ENGLAND", "PORTUGAL", "CHILE", "SLOVENIA"]
TEST_OPTIONS = []

def check_letter(user_guess, current_word, current_state):
    user_guess = user_guess.upper()
    if user_guess in current_word:
        updated_state = generate_state(current_word, user_guess, current_state)
    else:
        return 0

    return updated_state


def generate_state(current_word, user_guess = "", state = []):
    word_size = len(current_word)
    current_word = current_word.upper()
    instance_indexes = []

    if len(state) == 0:
        for letter in current_word:
            if letter == " ":
                state.append(" ")
            elif letter.isalpha():
                state.append("_")
            else:
                raise ValueError

    if user_guess == "":
        return state
    else:
        for index in range(word_size):
            if current_word[index] == user_guess:
                instance_indexes.append(index)

        for index in instance_indexes:
            state[index] = user_guess

    return state


def validate_letter_input(already_picked = []):
    while True:
        user_guess = input("Guess: ")
        user_guess = user_guess.upper()

        if user_guess in already_picked:
            print("Already picked this letter.")

        elif not user_guess.isalpha() or len(user_guess) > 1:
            print("Not a valid letter.")

        else:
            return user_guess


def play_again():
    while True:
        user_choice = input("Play again? (Y/N) ")
        user_choice = user_choice.upper()

        if user_choice == "Y":
            return True
        else:
            return False


def main():
    death_counter = 0
    already_picked = []
    current_word = random.choice(WORD_OPTIONS)
    current_state = generate_state(current_word)

    while True:
        print(" ".join(current_state))
        print()
        print("Already picked: " + ", ".join(already_picked))
        print(f"Death counter: {death_counter}")
        print()

        user_guess = validate_letter_input(already_picked)
        already_picked.append(user_guess)

        if check_letter(user_guess, current_word, current_state) == 0:
            death_counter += 1
        else:
            current_state = check_letter(user_guess, current_word, current_state)

        if death_counter == TRIES_LIMIT:
            print("FAIL")
            print(f"The word was: {current_word}")

            if play_again():
                death_counter = 0
                already_picked = []
                current_word = random.choice(WORD_OPTIONS)
                current_state = generate_state(current_word, user_guess = "", state = [])
            else:
                break

        elif "_" not in current_state:
            print()
            print(" ".join(current_state))
            print("WIN")

            if play_again():
                death_counter = 0
                already_picked = []
                current_word = random.choice(WORD_OPTIONS)
                current_state = generate_state(current_word, user_guess = "", state = [])
            else:
                break


if __name__ == "__main__":
    main()


        

