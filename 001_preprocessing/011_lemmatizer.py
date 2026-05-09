from nltk.stem import WordNetLemmatizer


wn_lemmatizer = WordNetLemmatizer()

print(f'Connecting after lemmatizer: {wn_lemmatizer.lemmatize("connecting", pos="v")}')