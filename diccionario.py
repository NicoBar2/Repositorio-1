def length_words(sentence):

    words = sentence.split()
    lengths = map(len, words)
    return dict(zip(words, lengths))

print(length_words('Welcome to Python'))