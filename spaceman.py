import random


def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.

    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed): 
    '''
        A function that checks if all the letters of the secret word have been guessed.

        Args:
            secret_word (string): the random word the user is trying to guess.
            letters_guessed (list of strings): list of letters that have been guessed so far.

        Returns: 
            bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    #pass

    found = True
    for char in secret_word:
      if char not in letters_guessed:
        found = False
        break 
    return found      

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.

    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''
    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    # pass

    display_word = ""

    for char in secret_word:
      #check if char is a letter from alpahabet
      if char in letters_guessed:
        display_word += char
      else:
        display_word += "_"
    return display_word
    

def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word

    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise

    '''
    #TODO: check if the letter guess is in the secret word
    #pass

    if guess in secret_word:
      return True
    else:
      return False  

  

      


def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    '''
    letters_guessed = []
    guesses = 0
    running = True
    

    print("Welcome to spaceman!")
    print(f"The secret word contains: {len(secret_word)} letters")

    print("You get 7 incorrect guesses, please enter one letter per round")
    
    while running:
      input_letter = input("Enter a letter = ")
      while len(input_letter) != 1 or len(input_letter) == "":
        print("Try again! Only one letter.")
        input_letter = input("Enter a letter = ")
          

      if is_guess_in_word(input_letter, secret_word):
        print("Your guess appears in the word!")
        letters_guessed.append(input_letter)
      else:
        print("Guess again")
        guesses += 1  

      #TODO: show the guessed word so far
      print(f"Guessed word so far: {get_guessed_word(secret_word, letters_guessed)}")

      #TODO: check if the game has been won or lost
      if is_word_guessed(secret_word, letters_guessed):
        running = False
        #user wins
      else:
        #user loses  
        if guesses == 7:
          print("You failed to guess the word.")
          print(f"The secret word is {secret_word}.")
          running = False
      


   
      
      

#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)
