import random
import hangman_words
import hangman_art


print(hangman_art.logo)
end_of_game = False
# word_list = ['ram','shyam','sitaram']

chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)
word_length = len(chosen_word)

lives=6

display = []
for _ in range(word_length):
    # display += "_"
    display.append("_")
print(display)


while not end_of_game:
    guess=input("Guess a letter:").lower()

    if guess in display:
        print(f'you`ve already guessed {guess}')
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f'you guessed {guess} , that`s not in the word. you loose a live ')
        lives-=1
        if lives==0:
            end_of_game=True
            print("You Lose")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game=True
        print("You Win!")

    print(hangman_art.stages[lives])