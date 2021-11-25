import winsound
# while True used to make the game run over and over
while True:
    hiddenWord = "san francisco"
    done = False
    guesses = []
    lives = 3

    """ loop to print blank spaces where user hasn't guessed the letter;
    meaning initially, the output will be completely blank spaces till
     user inputs a letter that exists in hiddenWord.
     Every input is appended to the guesses list """
    while done is False:
        for letter in hiddenWord:
            if letter in guesses:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        userInput = input(f"\nPlease guess any letter of the hidden word: ({lives} lives): ")
        guesses.append(userInput)
        # number of lives decreases by one if wrong letter is input
        if userInput not in hiddenWord:
            lives -= 1
            winsound.Beep(500, 500)
            if lives == 0:
                break
        else:
            winsound.MessageBeep(-1)

        done = True
        for letter in hiddenWord:
            if letter not in guesses:
                done = False
    #
    if done:
        print(" ".join(hiddenWord))
        winsound.MessageBeep(-1)
        print(f"Congrats! {hiddenWord.upper()} is the word!!")

    else:
        # if user failed, hidden word is displayed with some swag :) using beep sound
        # beep() is used from the winsound lib
        print("Oops.. Game over! the hidden word is ")
        for char in hiddenWord:
            print(char.upper(), end=" ")
            winsound.Beep(900, 100)
        print("\nTry again next time. Enter 0 to quit")
    userInput = input("\nPlay again? Y/N: ")
    if userInput == 'N' or userInput == 'n':
        break

    print("\n")
    print("\n")