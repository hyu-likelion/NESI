def countAlphabet():
    alphabet = {"a": 0, "b": 0, "c":0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0,"p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}
    list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o" , "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    word = input().lower()
    for i in range(len(word)):
        alphabet[word[i]] += 1
    frequent = -1
    for n in range(len(alphabet)):
        if frequent < alphabet[list[n]] and alphabet[list[n]] > 0:
            frequent = alphabet[list[n]]
            result = list[n]
        elif frequent == alphabet[list[n]]:
            result = '?'
    return result.upper()

x = countAlphabet()
print(x)
