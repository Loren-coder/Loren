# 5. User input 2


word=input("Give me a word")

score = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1,  "f": 4,
         "g": 2, "h": 4,"i": 1, "j": 8, "k": 5, "l": 1,
         "m": 3, "n": 1, "o": 1, "p": 3, "q": 10, "r": 1,
         "s": 1, "t": 1, "u": 1, "v": 4, "w": 4, "x": 8,
         "y": 4,"z": 10}

sum=sum(score[i] for i in word)
print(sum)

# Feedback - Repaired print statement. This works and is correct, but will throw an error if I give this anything
# that is not incorporated in your dictionary. For example, if I give it a number "1", it kicks out
# a key error: KeyError: '1'
# this means it cannot find the key "1" inside the dictionary, you need to catch that otherwise issues arise.