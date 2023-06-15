import math
import pandas as pd

# Russian text
with open('textRU.txt') as f:
    symbols = f.read()
letter_frequency = pd.Series(list(filter(str.isalpha, symbols.lower()))).value_counts()
# print(letter_frequency)
f.close()

for key in letter_frequency: print(key)