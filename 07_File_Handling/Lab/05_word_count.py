# Read words to search
with open("words.txt") as file:
    words = file.read().split()

# Read the content of text, lowercase -> case-insensitive
with open("text.txt") as text:
    text = text.read().lower()

# Extract all words in a list with RegEx
import re
words_in_text = re.findall(r'\b\w+\b', text)

words_count = {}
for word in words:
    word = word.lower()
    words_count[word] = words_in_text.count(word)


with open("output.txt", mode='a') as output:
    for word, count in sorted(words_count.items(), key=lambda x: -x[1]):
        output.write(f"{word} - {count}\n")
