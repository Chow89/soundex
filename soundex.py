def soundex(word):
    res = word[0]
    word = word.upper()[1:]
    n = 1
    code = {
        "A": 0,
        "B": 1,
        "C": 2,
        "D": 3,
        "E": 0,
        "F": 1,
        "G": 2,
        "H": 0,
        "I": 0,
        "J": 2,
        "K": 2,
        "L": 4,
        "M": 5,
        "N": 5,
        "O": 0,
        "P": 1,
        "Q": 2,
        "R": 6,
        "S": 2,
        "T": 3,
        "U": 0,
        "V": 1,
        "W": 0,
        "X": 2,
        "Y": 0,
        "Z": 2
    }
    for c in word:
        num = code[c]
        if num != 0 and num != res[n-1]:
            res += str(num)
            n += 1
    while len(res) < 4:
        res += "0"
    return res[0:4]

print(soundex("Github"))