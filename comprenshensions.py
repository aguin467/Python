## slow
tokens = []
for word in sentence:
    tokens.append(word.lower())
## faster
[word.lower() for word in sentence]