"""
tokenization refers to separating words or chunks from a given dataset.
or dividing the given data into small parts, components, words, sentences, whatever component the use case demands.
"""

var_text = 'hello, this is python coding'


#   1. Using Split


#   the simplest and naive way to split the above text into smaller parts is to use split() function
#   this returns a list of words separated by empty spaces
token_text = var_text.split()

print(token_text)   #   lets see the list of words separated

"""
the above method is straight forward but not fully effective.
"""

#   2. using regex

"""
lets try tokenizing using regex library
This is another way to tokenize using regular expressions
"""


import re

var_text = 'hello, this is python coding!'

token_text = re.findall(r'\w+', var_text)

print(token_text)


"""
using regex, you may notice that the previous method of using split() included any attached puntutation with the words.
"""

#   3. character tokenization

var_text = 'hello, this is python coding!'

char_tokens = list(var_text)
print(f'character tokens: {char_tokens}')
