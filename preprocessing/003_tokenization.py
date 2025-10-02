"""
tokenization refers to separating words from a given dataset.
or dividing the given data into small parts, components, words, sentences, whatever component the use case demands.
"""

var_text = 'hello, this is python coding'


#   one way to split the above text into smaller parts is to use split() function
token_text = var_text.split()

print(token_text)   #   lets see the list of words separated

"""
the above method is straight forward but not fully effective.
lets try tokenizing using regex library
"""


import re

var_text = 'hello, this is python coding!'

token_text = re.findall(r'\w+', var_text)

print(token_text)