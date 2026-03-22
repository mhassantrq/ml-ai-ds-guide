"""
Regular expressions are easy way to extract information from any given text

Regular expression rules, commands and shortcuts
Meta characters

.           any character
?           none or one occurance of given character
+           one or more occurance of given character
*           zero or more occurance of given character
^           indicating the start of string. however, when placed inside square brackets, idicates that what may not be present in text
$           indicates the end of string

Combination of characters to make it easier

\w          all the characters in a-z, A-Z and 0-9 and underscore
\W          any characters except a-z, A-Z, and 0-9

\d          all characters in 0-9
\D          any character except 0-9

\s          blank space

{n}         n indicates the number of times the previous character in expression may occur in text
|           or, specifying the choice between characters
[]          square brackets
"""

import re

text = "this is a sentence to check for regular expressions"