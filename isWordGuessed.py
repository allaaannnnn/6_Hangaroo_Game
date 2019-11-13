def isWordGuessed(secretWord, lettersGuessed):
    correctLetters = 0
    wordLetters = list(secretWord)
    for i in wordLetters:
        if i in lettersGuessed:
            correctLetters = correctLetters + 1
    if correctLetters == len(wordLetters):
        print ('True')
    else:
        print ('False')