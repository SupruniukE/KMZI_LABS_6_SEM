import math
import pandas as pd

def shannon_entropy(text):
    entropy = 0
    for p in text: 
        entropy += p * math.log(p, 2)
    entropy *= -1
    return entropy


# Russian text
with open('textRU.txt') as f:
    symbols = f.read()
letter_frequency = pd.Series(list(filter(str.isalpha, symbols.lower()))).value_counts(normalize=True)
print(letter_frequency)
f.close()

russian_entropy = shannon_entropy(letter_frequency)
print("Russian entropy:", russian_entropy)

symbols_cp1251 = symbols.encode("cp1251")

russian_binary = ''.join(format(x, 'b') for x in symbols_cp1251)
letter_frequency = pd.Series(list(russian_binary)).value_counts(normalize=True)
russian_binary_entropy = shannon_entropy(letter_frequency)
print("Russian binary entropy:", russian_binary_entropy)


# English text
with open('textEN.txt') as f:
    symbols = f.read()
letter_frequency = pd.Series(list(filter(str.isalpha, symbols.lower()))).value_counts(normalize=True)
# print(letter_frequency)
f.close()

english_entropy = shannon_entropy(letter_frequency)
print("English entropy:", english_entropy)

symbols_ascii = symbols.encode("ascii")

english_binary = ''.join(format(x, 'b') for x in symbols_ascii)
letter_frequency = pd.Series(list(english_binary)).value_counts(normalize=True)
english_binary_entropy = shannon_entropy(letter_frequency)
print("English binary entropy:", english_binary_entropy)


# FIO
FIO_ru = "Супрунюк Евгений Андреевич"
FIO_en = "Supruniuk Evgeny Adreevich"

FIO_ru_cp1251 = FIO_ru.encode("cp1251")
bytes_FIO_ru_cp1251 = bytes(FIO_ru_cp1251)
FIO_en_ascii = FIO_en.encode("ascii")
bytes_FIO_en_ascii = bytes(FIO_en_ascii)

print("Amount of Information FIO RU:", russian_entropy * len(FIO_ru))
print("Amount of Information FIO RU bin:", russian_binary_entropy * len(FIO_ru))
# print("Amount of Information FIO RU ascii:", russian_binary_entropy * len(bytes_FIO_ru_cp1251))

print("Amount of Information FIO EN:", english_entropy * len(FIO_en))
print("Amount of Information FIO EN bin:", english_binary_entropy * len(FIO_en))
# print("Amount of Information FIO EN ascii:", english_binary_entropy * len(bytes_FIO_en_ascii))

def count_information_with_mistake(entropy, N, q):
    p = 1 - q
    try:
        result = -p * math.log(p, 2) - q * math.log(q, 2)
    except ValueError:
        result = float('nan')
    return N * (1 - result)

print(f"RU Error 0,1: {count_information_with_mistake(russian_entropy, len(FIO_ru), 0.1)}")
print(f"RU Error 0,5: {count_information_with_mistake(russian_entropy, len(FIO_ru), 0.5)}")
print(f"RU Error 1: {count_information_with_mistake(russian_entropy, len(FIO_ru), 1)}")

print(f"EN Error 0,1: {count_information_with_mistake(english_entropy, len(FIO_en), 0.1)}")
print(f"EN Error 0,5: {count_information_with_mistake(english_entropy, len(FIO_en), 0.5)}")
print(f"EN Error 1: {count_information_with_mistake(english_entropy, len(FIO_en), 1)}")