from random import choice

word_list = ['apple', 'banana', 'orange', 'grape', 'kiwi', 'ananas', 'laptop']


def replace_characters(guessed_str, guess, word):
    """
        Function to replace chars in guessed_str with real characters
        guessed_str: string
        guess: string
        word: string
        returns: string
    """
    count_of_guessed_characters = word.count(guess)
    new_str = guessed_str
    index_of_letter = 0

    while count_of_guessed_characters > 0:
        index_of_letter = word.index(guess, index_of_letter)
        new_str = new_str[:index_of_letter] + guess + new_str[index_of_letter + 1:]
        index_of_letter += 1
        count_of_guessed_characters -= 1

    return new_str


def guess_the_world():
    """
    Function for guessing a randomly selected word
    :return: None
    """
    attempts = input('Enter the number of attempts: ')
    random_word = choice(word_list)
    wasted_attempts = 0

    if not attempts.isdigit():
        print('Wrong number of attempts')
        return

    guessed_letters = '*' * len(random_word)

    while wasted_attempts <= int(attempts):
        guess = input('Guess a letter or type all word: ').lower()

        if len(guess) > 1:
            if guess == random_word:
                print('Congratulations, you guessed!')
                break

            print('You didn\'t guess the word')
            wasted_attempts += 1
        else:
            if guess in random_word:
                # replace guessed_letters with real characters
                guessed_letters = replace_characters(guessed_letters, guess, random_word)
                print(guessed_letters)

                if guessed_letters == random_word:
                    print('Congratulations, you guessed!')
                    break
            else:
                print('There is no such letter')
                wasted_attempts += 1

    else:
        print('Unfortunately, attempts to guess the word have ended. Thanks for game.')


guess_the_world()
