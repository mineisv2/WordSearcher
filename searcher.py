width = 8
height = 7

letters = [["T", "T", "L", "C", "T", "S", "A", "E", "F"],
           ["H", "U", "G", "O", "N", "T", "O", "F", "A"],
           ["A", "R", "B", "R", "A", "N", "G", "E", "M"],
           ["N", "K", "O", "N", "D", "F", "I", "N", "I"],
           ["K", "E", "E", "G", "R", "A", "V", "Y", "L"],
           ["S", "Y", "L", "D", "N", "M", "E", "T", "Y"],
           ["X", "I", "E", "D", "I", "N", "N", "E", "R"],
           ["V", "P", "I", "L", "G", "R", "I", "M", "S"]]

words = ["THANKS", "GIVE", "FEAST", "PILGRIMS", "DINNER", "TURKEY", "FAMILY", "CORN", "GRAVY"]

def vertCheck(posX, posY, word):
    word = list(word)
    try:
        for i in range(len(word)):
            if letters[posY+i][posX] == word[i]:
                pass
            else:
                break
        else:
            print(str("".join(word)) + " (" + str(posX) + ", " + str(posY) + ") " + "DOWN")
    except IndexError:
        pass
    try:
        for i in range(len(word)):
            if letters[posY-i][posX] == word[i]:
                pass
            else:
                break
        else:
            print(str("".join(word)) + " (" + str(posX) + ", " + str(posY) + ") " + "UP")
    except IndexError:
        pass

def horizCheck(posX, posY, word):
    word = list(word)
    try:
        for i in range(len(word)):
            if letters[posY][posX+i] == word[i]:
                pass
            else:
                break
        else:
            print(str("".join(word)) + " (" + str(posX) + ", " + str(posY) + ") " + "RIGHT")
    except IndexError:
        pass
    try:
        for i in range(len(word)):
            if letters[posY][posX-i] == word[i]:
                pass
            else:
                break
        else:
            print(str("".join(word)) + " (" + str(posX) + ", " + str(posY) + ") " + "LEFT  ")
    except IndexError:
        pass

def letterFinder(letter):
    for i in range(len(letters)):
        for j in range(len(letters[i])):
            if letters[i][j] == letter:
                yield (j, i)

for i in range(len(words)):
    for j in letterFinder(words[i][0]):
        vertCheck(j[0], j[1], words[i])
        horizCheck(j[0], j[1], words[i])

for i in range(len(letters)):
    print(letters[i])
