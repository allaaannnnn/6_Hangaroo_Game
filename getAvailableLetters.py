def getAvailableLetters(lettersGuessed):
    alphabet = ('abcdefghijklmnopqrstuvwxyz')
    letters = list(alphabet)
    availableLetters = str()
    for i in letters:
        if i in lettersGuessed:
            letters.remove(i)
    return availableLetters.join(letters)