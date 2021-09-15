def countLetters(string):
    return string, len(string)


if __name__ == '__main__':
    word = input("Please enter a string:")
    print(countLetters(word))

    wordList = ('Matt', 'Abbi', 'Soccer', 'Logan', 'Football', 'Coding', 'Python', 'HelloWorld', 'MAPPING')

    wordLen = map(countLetters, wordList)

    print(list(wordLen))
