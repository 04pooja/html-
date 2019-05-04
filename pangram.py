from string import ascii_lowercase
def pangram(sentence):
    return set(ascii_lowercase).issubset(sentence)
sentence=str(input("enter your string:"))
print(pangram(sentence))
