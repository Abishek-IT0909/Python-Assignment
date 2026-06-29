def convert_to_uppercase(strings):
    return list(map(lambda x: x.upper(), strings))

words = ["mango", "orange", "television"]
res = convert_to_uppercase(words)
print(res)