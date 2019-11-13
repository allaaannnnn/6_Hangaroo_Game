def Hangaroo(secretWord):
    
##INITIALIZATIONS##
    secretWord = secretWord.lower()
    wordLetters = list(secretWord)
    notwordLetters = []
    lettersGuessed = []
    correctLetters = 0
    mistakes = 0
    guessWord = []
    word = str()
    alphabet = ('abcdefghijklmnopqrstuvwxyz')
    letters = list(alphabet)
    availableLetters = str()
    for i in alphabet:
        if i not in wordLetters:
            notwordLetters.append(i)

##INSTRUCTIONS##  
    print ('Welcome to Hangaroo')
    x = str(input('Enter 1 to start the game!\n'))
    if x != '1':
        return
    else:
            print ('\nThe game has started,')
            print ('Enter "guess" to guess the word')
            print ('Enter "letters" to view available letters')
            print ('Enter "quit" to quit the game')
            print ('Enter a letter you want to guess')
            for k in secretWord:
                if k in lettersGuessed:
                    guessWord.append(k)
                else:
                    guessWord.append(' _ ')
            print (word.join(guessWord))
            
##START##
            while correctLetters != len(wordLetters):
                guessWord = []
                guess = str(input())
                guess = guess.lower()
                
##GUESS##
                if guess == 'guess':
                    for k in secretWord:
                        if k in lettersGuessed:
                            guessWord.append(k)
                        else:
                            guessWord.append(' _ ')
                    print (word.join(guessWord))
                    answer = input('Enter your final answer:\nType "cancel" to return.\n')
                    answer = answer.lower()
                    if answer == secretWord:
                        print ('\nCongratulations,', secretWord, 'is the correct answer!')
                        print ('Number of Mistakes:', mistakes)
                        return
                    if answer == 'cancel':
                        pass
                    else:
                        print ('\nSorry, the correct answer is:', secretWord)
                        print ('Number of Mistakes:', mistakes)
                        return
                    
##LETTERS##
                if guess == 'letters':
                    for j in letters:
                        if j in lettersGuessed:
                             letters.remove(j)
                    print ('The available letters are:', availableLetters.join(letters))
              
##QUIT##
                if guess == 'quit':
                    return
                
##REPEATED##
                if guess in lettersGuessed:
                    print ('You already guessed that letter! Try again.')
                    
##CORRECT##
                if ((guess in wordLetters) and (guess not in lettersGuessed)):
                    lettersGuessed.append(guess)
                    for k in secretWord:
                        if k in lettersGuessed:
                            guessWord.append(k)
                        else:
                            guessWord.append(' _ ')
                    print ('\n',word.join(guessWord))
                    correctLetters = correctLetters + secretWord.count(guess)
                  
##INCORRECT##
                if ((guess in notwordLetters) and (guess not in lettersGuessed)):
                    print ('The entered letter is not in the secret word.')
                    lettersGuessed.append(guess)
                    mistakes = mistakes + 1
                    
##END##
            if correctLetters == len(wordLetters):
                print ('\nCongratulations,', secretWord, 'is the secret word!')
                print ('Number of Mistakes:', mistakes)

                