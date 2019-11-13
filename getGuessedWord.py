def getGuessedWord(secretWord,lettersGuessed):
    wordLetters = list(secretWord)
    guessWord = []
    correct = []
    word = str()
    for i in lettersGuessed:
        if i in wordLetters:
            correct.append(i)
    for i in secretWord:
        if i in lettersGuessed:
            guessWord.append(i)
        else:
            guessWord.append(' _ ')
    return word.join(guessWord)