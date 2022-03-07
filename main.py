from replit import clear
import hangman_words
import hangman_art

import random
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

print(hangman_art.logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

end_of_game = False
lives = 6

while not end_of_game and lives > 0:
    guess = input("Guess a letter: ").lower()

    clear()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
 

    if guess in display:
      print("You've already guessed this letter, please guess again")

    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} is not in the word. You have {lives} lives left... Guess again!")
        if lives == 0:
         end_of_game = True
         print("You LOSE!")
         print(chosen_word)
      

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")


    #Check if there are no more "_" left in 'display'. Then all letters have been guessed.
    if "_" not in display:
        end_of_game = True
        print("You win.")
  
    print(hangman_art.stages[lives])