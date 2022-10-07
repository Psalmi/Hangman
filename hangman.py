import random
from words import word_list
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

print(logo)

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


chosen_word = random.choice(word_list)

lives = 6

#testing the code
#print(f"psst, the solution is {chosen_word}")

# creating the blanks
display = []
word_length = len(chosen_word)

for i in chosen_word:
        display.append("_")

# creating the guess the letter logic

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"you have already guessed {guess}")
        
        #print(display)

    for position in range((word_length)):
        letter = chosen_word[position]
        #print(f"Current position: {position} \n Current letter: {letter} \n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    
    print(f"{' '.join(display)}")      
        
    if guess not in chosen_word:
        print(f"you have guessed {guess}, that is not in the word. You lose a life. ")
        lives -= 1   
        if lives == 0:
            end_of_game = True
            print("You lose!")
            print(logo)
            
         
    
    # print(display)
            
    if "_" not in display:
        end_of_game = True
        print("you win!")
        print(logo)
        
        
        
    print(stages[lives])
        







    

