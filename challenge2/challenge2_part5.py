# Using the following dictionary (or a similar one you found on the internet), ask the user for a word, and compute the Scrabble word score for that word (Scrabble is a word game, where players make words from letters, each letter is worth a point value), steal this code from the internet, format it and make it work:
#
# letter_scores = {
#     "a": 1, "e": 1, "i": 1, "o": 1,"u": 1, "l": 1, "n": 1, "r": 1, "s": 1, "t": 1,
#     "d": 2, "g": 2,
#     "b": 3, "c": 3, "m": 3, "p": 3,
#     "f": 4, "h": 4, "v": 4, "w": 4, "y": 4,
#     "k": 5,
#     "j": 8, "x": 8,
#     "q": 10, "z": 10
# }
# def scrabble_score(word):
#     total = 0
#     for i in word:
#         total = total+letter_scores[i.lower()]
#     return total
#word = input("What is your word?")
# print (scrabble_score(word))