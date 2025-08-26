#This is a game of Hangman. I have a word bank that I created related to technology, and the computer selects a random word to use for the game. You have 10 attempts to guess the word by guessing the letters individually. If you guess right, the blank line is replaced by the correct corresponding letter(s). If you guess wrong, the number of attempts you have left decreases by 1. If you guess wrong 10 times, you lose. If you guess the correct word before you run out of attempts, you win.


import random #library import to select a random word

def computer_choice(): #function that contains the words
    secret_words = ["python", "coding", "robotics", "programming", "technology", "computer", "software", "network", "animation", "controller", "internet", "website", "tablet", "browser", "language", "media", "robot", "device", "engineering", "gadget", "electronics", "mechanics", "computing", "machine", "invention"] #word bank
    word = random.choice(secret_words) #randomly selected word from the word bank
    return word #this word will be used for the rest of the program

word = computer_choice() #defines "word" as the random word given by the function
letters = list(word) #splits the word apart so that each letter is a term of the list
n = len(word) #defines the length of the list/word
guessed_letters = ["_" for x in letters] #replaces every letter with an underscore (_). This will be replaced by letters as the player guesses each letter
attempts = 10 #defines the number of attempts

print("Welcome to a Game of Hangman!") #introduction
print("This word has " + str(n) + " letters! You have 10 chances to guess the word. If you guess wrong letters 10 times, you lose. If you guess all the letters in the word correctly, you win the game!") #in the description I converted the number to a string so that it could be printed
print(guessed_letters) #gives a visual representation of how many letters are in the word

while attempts > 0: #runs the loop while the player has more than 0 attempts
    guess = input("Guess a letter:") #allows for the player to input 1 letter
    found = False #boolean is used to determine whether there are letters in the word. It is set as false initially so that when the letter is found, it becomes true, and then goes back to false once the loop repeats.
    for i in range(len(letters)): #checks each term of the list
        if guess == letters[i]: #if the input matches 1 or more of the letters of the word...
            print("Correct! There is a " + guess + " in position " + str(i+1) + ".") #prints out which position contains that guessed letter. Changes number to string again for printing.
            guessed_letters[i] = guess #replaces the underscore with the guessed letter for any position "i" that contains the letter
            print (guessed_letters) #prints the newly updated list of underscore(s)/letter(s)
            found = True #boolean changed to true, since letter was found
    
    if found == False: #if boolean stays false and no letter was found
        print("Sorry, there isn't a '" + guess + "' in this word.") #prints the guessed letter and says it's not there
        attempts -= 1 #deducts 1 attempt
        print(guessed_letters) #prints the current list of underscore(s)/letter(s)

    if guessed_letters == letters: #once all the dashes are replaced by the correct corresponding letters
        print("You won the game! You guessed the word: " + word) #the player wins the game and the correct word is confirmed
        break #the while loop ends

    if attempts > 0: #when the attempts are greater than 0
        print("You now have " + str(attempts) + " attempts left.") #prints the number of attempts remaining each round
        
    else: #if attempts == 0
        print("You lost: You ran out of attempts! The word is '" + word + "'") #the player lost and the word is revealed
