import random

def computer_choice():
    secret_words = ["python", "coding", "robotics", "programming", "technology", "computer", "software", "network", "animation", "controller", "internet", "website", "tablet", "browser", "language", "media", "robot", "device", "engineering", "gadget", "electronics", "mechanics", "computing", "machine", "invention"]
    word = random.choice(secret_words)
    return word

word = computer_choice()
letters = list(word)
n = len(word)
guessed_letters = ["_" for x in letters]
attempts = 10

print("Welcome to a Game of Hangman!")
print("This word has " + str(n) + " letters! You have 10 chances to guess the word. If you guess wrong letters 10 times, you lose. If you guess all the letters in the word correctly, you win the game!")
print(guessed_letters)

while attempts > 0:
    guess = input("Guess a letter:")
    found = False
    for i in range(len(letters)):
        if guess == letters[i]:
            print("Correct! There is a " + guess + " in position " + str(i+1) + ".")
            guessed_letters[i] = guess
            print (guessed_letters)
            found = True
    
    if not found:
        print("Sorry, there isn't a '" + guess + "' in this word.")
        attempts -= 1
        print(guessed_letters)

    if guessed_letters == letters:
        print("You won the game! You guessed the word: " + word)
        break

    if attempts > 0:
        print("You now have " + str(attempts) + " attempts left.")
        
    else:
        print("You lost: You ran out of attempts! The word is '" + word + "'")

   

            
