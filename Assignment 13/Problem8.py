#8. Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary

text = "python is great and python is easy"
words = text.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print("Word frequency:", freq)