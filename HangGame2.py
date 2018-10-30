word = "test"
# guess = "a"
# Enter Guess:
wrong_guesses = 0;
name = input("What is your name? ").lower()
guess = ""
print("Hey, " + name + " lets play hangman!")

while (wrong_guesses > 6) == (guess == word):
    c = input("What is your guess? ")
    guess += c
    print(wrong_guesses)
    if c in word:
        print("Correct!")
        nguess = ""
        for s in word:
            if s == c:
                nguess += c;
            else:
                nguess += " ";
        guess = nguess;
    else:
        print("You Failed.")
        wrong_guesses += 1;
    
if wrong_guesses > 6:
    print("You Lose :(")
else:
    print("You won :)")
