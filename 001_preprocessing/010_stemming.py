"""
stemming is a technique used to cut or stem a word to its root word.
this way, multiple variations of a root word can be treated as same.

such as cutting connect, connects, connecting, connected, connection etc to a base common word connect.

however, this may not always be the case. often times, cutting words can lead to such a root word which may not be a real word.
this is basic difference between stemming and lemmatization which is covered in the next file.
"""

from nltk.stem import PorterStemmer, SnowballStemmer, LancasterStemmer

w_list = ['connect', 'connects', 'connecting', 'connected', 'connection', 'connections']

#   1.  SnowBall Stemmer

sb_stemmer = SnowballStemmer('english')
for word in w_list:
    print(f'{word} after snowball stemming: {sb_stemmer.stem(word)}')


#   2.  Porter Stemmer

p_stemmer = PorterStemmer()

for word in w_list:
    print(f'{word} after porter stemming: {p_stemmer.stem(word)}')


#   2.  Lancaster Stemmer

l_stemmer = LancasterStemmer()

for word in w_list:
    print(f'{word} after lancaster stemming: {l_stemmer.stem(word)}')
