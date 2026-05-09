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
