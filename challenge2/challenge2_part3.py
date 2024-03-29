# Using this string:
string = 'hi dee hi how are you mr dee'

# Count the occurrence of each word, and print the word plus the count (hint, you might want to "split" this into a
# list by a white space: " ").
def word_count(str):
    counts = dict()
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

print(word_count('hi dee hi how are you mr dee'))