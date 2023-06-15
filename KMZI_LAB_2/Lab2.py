import math
import re

def shannon_entropy(text):
    # Remove non-letter characters from the text
    text = re.sub('[^a-zA-Zа-яА-Я01]', '', text).lower()

    # Create a dictionary to store the count of each letter in the text
    counts = {}
    for char in text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    # Calculate the probability of each letter
    probs = []
    for count in counts.values():
        prob = count / len(text)
        probs.append(prob)

    # Calculate the entropy using the probability of each letter
    entropy = 0
    for prob in probs:
        entropy -= prob * math.log(prob, 2)

    # Calculate the sum of probabilities
    sum_probs = sum(probs)
    if sum_probs > 1:
        sum_probs = 1

    return entropy, sum_probs


def count_characters(text):
    # Create a dictionary to store the count of each letter in the text
    counts = {}
    for char in text:
        if char.isalpha():
            if char.lower() in counts:
                counts[char.lower()] += 1
            else:
                counts[char.lower()] = 1

    # Sort the letters by their count in descending order
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

    # Print the counts of each letter
    for char, count in sorted_counts:
        print(f"{char}: {count}")


def count_inf(entropy, N):
    return entropy * N


def count_information_with_mistake(entropy, N, p):
    q = 1 - p
    try:
        result = -p * math.log(p, 2) - q * math.log(q, 2)
    except ValueError:
        result = float('nan')
    print(result)
    return N * (1 - result)


# Read the English and Cyrillic text from files
with open("textEN.txt", "r", encoding="utf-8") as f:
    english_text = f.read()
with open("textRU.txt", "r", encoding="utf-8") as f:
    cyrillic_text = f.read()

# Calculate the entropy and count the characters of the English and Cyrillic text
english_entropy, english_sum_probs = shannon_entropy(english_text)
cyrillic_entropy, cyrillic_sum_probs = shannon_entropy(cyrillic_text)
print("English:")
count_characters(english_text)
print(f"Sum of probabilities: {english_sum_probs}")
print(f"Entropy: {english_entropy}")

# Convert English text to binary
byte_arr = bytearray(english_text, 'utf-8')
binary_text = ""
for byte in byte_arr:
    binary_rep = bin(byte)  # convert to binary representation
    binary_text += binary_rep[2:]  # remove prefix "0b" and add to binary text

# Calculate the entropy of the binary representation
binary_entropy_eng = shannon_entropy(binary_text)[0]
print(f"Binary entropy: {binary_entropy_eng}")
print()

print("Cyrillic:")
count_characters(cyrillic_text)
print(f"Sum of probabilities: {cyrillic_sum_probs}")
print(f"Entropy: {cyrillic_entropy}")

# Convert Cyrillic text to binary
byte_arr = bytearray(cyrillic_text, 'utf-8')
binary_text = ""
for byte in byte_arr:
    binary_rep = bin(byte)  # convert to binary representation
    binary_text += binary_rep[2:]  # remove prefix "0b" and add to binary text

# Calculate the entropy of the binary representation
binary_entropy_ru = shannon_entropy(binary_text)[0]
print(f"Binary entropy: {binary_entropy_ru}")


NPS_ru = "Дащинский Максим Леонидович";
NPS_en = "Dashchinskiy Maksim Leonidovich";

NPS_ru_cp1251 = NPS_ru.encode("cp1251")
bytes_NPS_ru_cp1251 = bytes(NPS_ru_cp1251)
NPS_en_ascii = NPS_en.encode("ascii")
bytes_NPS_en_ascii = bytes(NPS_en_ascii)

print(f"Amount of Information SNP RU: {count_inf(cyrillic_entropy, len(NPS_ru))}")
print(f"Amount of Information SNP RU bin: {count_inf(binary_entropy_ru, len(NPS_ru))}")
print(f"Amount of Information SNP RU ascii: {count_inf(binary_entropy_ru, len(bytes_NPS_ru_cp1251))}")

print(f"Amount of Information SNP EN: {count_inf(english_entropy, len(NPS_en))}")
print(f"Amount of Information SNP EN bin: {count_inf(binary_entropy_eng, len(NPS_en))}")
print(f"Amount of Information SNP EN ascii: {count_inf(binary_entropy_eng, len(bytes_NPS_en_ascii))}")


print(f"RU Error 0,1: {count_information_with_mistake(binary_entropy_ru, len(bytes_NPS_ru_cp1251), 0.9)}")
print(f"RU Error 0,5: {count_information_with_mistake(binary_entropy_ru, len(bytes_NPS_ru_cp1251), 0.5)}")
print(f"RU Error 1: {count_information_with_mistake(binary_entropy_ru, len(bytes_NPS_ru_cp1251), 1)}")

print(f"EN Error 0,1: {count_information_with_mistake(binary_entropy_eng, len(bytes_NPS_en_ascii), 0.9)}")
print(f"EN Error 0,5: {count_information_with_mistake(binary_entropy_eng, len(bytes_NPS_en_ascii), 0.5)}")
print(f"EN Error 1: {count_information_with_mistake(binary_entropy_eng, len(bytes_NPS_en_ascii), 1)}")
