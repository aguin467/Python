sentence = "Hello darkness my old friend."

## slow
tokens = []
for word in sentence:
    tokens.append(word.lower())
## faster
[word.lower() for word in sentence]


# my_items = map(my_function, my_list) Better way for a dictionary
