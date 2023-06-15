# Вариант 6
# Приложение 1
# Линейный конгруэнтный генератор
# a = 430, c = 2531, n = 11_979
# Приложение 2
# RC4 с n = 6 - размер блока (взял 8, чтобы можно было зашифровать/расшифровать английский текст)
# S-блок размера 2^n = (от 0 до 64)
# Ключ в виде десятичных чисел 1, 11, 21, 31, 41, 51
# i = 0, j = 0
# j = j + S(i) + K(i)
# S(i), S(j) = S(j), S(i)
# i = i + i

import time


def ReadFile(name_file):
    file_for_only_read = open(name_file, 'r', encoding="utf8")
    return file_for_only_read.read()


def GeneratingPseudorandomNumbersByMethodOfLinearCongruence(a, c, n, count_number, x=None):
    if x is None:
        x = 1
    if count_number is None:
        count_number = 5

    pseudorandom_numbers = []
    for i in range(count_number):
        x = (a * x + c) % n
        pseudorandom_numbers.append(x)
    return pseudorandom_numbers


def MixTableK(table_k, table_s):
    index_i = 0
    index_j = 0
    table_s_for_mixed = table_s[:]

    for i in range(len(table_k)):
        index_j = (index_j + table_s[index_i] + table_k[i]) % len(table_k)
        table_s_for_mixed[index_i], table_s_for_mixed[index_j] = table_s_for_mixed[index_j], table_s_for_mixed[index_i]
        index_i += 1
    mixed_table_k = table_s_for_mixed[:]
    return mixed_table_k


def GenerateTableSAndK(keys, buffer_size):
    table_s = [i for i in range(2 ** buffer_size)]
    table_k = ([i for i in keys] * (len(table_s) // len(keys) + 1))[:len(table_s)]
    return table_s, table_k


def GenerateRandomWords(mixed_table_s, number_of_random_numbers, buffer_size):
    module = 2 ** buffer_size
    index_i = 0
    index_j = 0
    random_words = []
    mixed_table_s_ = mixed_table_s[:]

    for i in range(number_of_random_numbers):
        index_i += 1
        index_j = (index_j + mixed_table_s[index_i]) % module
        mixed_table_s_[index_i], mixed_table_s_[index_j] = mixed_table_s_[index_j], mixed_table_s_[index_i]
        a = (mixed_table_s_[index_i] + mixed_table_s_[index_j]) % module
        random_words.append(mixed_table_s_[a])
    return random_words


def XORMessageAndKeyWords(message_list, keys_list, buffer_size):
    if len(message_list) > len(keys_list):
        keys_list = (keys_list * (len(message_list) // len(keys_list) + 1))[:len(message_list)]

    encrypt_messsage = []
    for index, elem in enumerate(zip(message_list, keys_list)):
        current_xor_number = ''
        elem_0_2 = (buffer_size - len(bin(elem[0])[2:])) * '0' + bin(elem[0])[2:]
        elem_1_2 = (buffer_size - len(bin(elem[1])[2:])) * '0' + bin(elem[1])[2:]
        for i in range(buffer_size):
            if elem_0_2[i] == elem_1_2[i]:
                current_xor_number += '0'
            else:
                current_xor_number += '1'
        encrypt_messsage.append(int(current_xor_number, 2))
    return encrypt_messsage


def main():
    a = 430
    c = 2531
    n = 11_979
    x = 1
    count_number = 15
    pseudorandom_numbers = GeneratingPseudorandomNumbersByMethodOfLinearCongruence(a, c, n, count_number, x)

    encrypt_time = time.time()
    keys = [1, 11, 21, 31, 41, 51]
    buffer_size = 8
    table_s, table_k = GenerateTableSAndK(keys, buffer_size)
    mixed_table_s = MixTableK(table_k, table_s)

    number_of_random_numbers = 10
    random_words = GenerateRandomWords(mixed_table_s, number_of_random_numbers, buffer_size)

    message = ReadFile('text_en.txt')
    message_10 = [ord(i) for i in message]

    encrypt_message_10 = XORMessageAndKeyWords(message_10, random_words, buffer_size)
    encrypt_message = ''.join([chr(i) for i in encrypt_message_10])
    encrypt_time = time.time() - encrypt_time

    decrypt_time = time.time()
    decrypt_message_10 = XORMessageAndKeyWords(encrypt_message_10, random_words, buffer_size)
    decrypt_message = ''.join([chr(i) for i in decrypt_message_10])
    decrypt_time = time.time() - decrypt_time

    print(f'----- Приложение 1. Линейный конгруэнтный генератор -----\n'
          f'Начальные настройки: a = {a}, c = {c}, n = {n}, x = {x}\n'
          f'Псевдослучайные число: {pseudorandom_numbers}\n\n'
          
          f'----- Приложение 2. Алгоритм RC4\n'
          f'Заполненная таблица S: {len(table_s)}\n{table_s}\n'
          f'Заполненная таблица K: {len(table_k)}\n{table_k}\n'
          f'Перемешанная таблица S: {len(mixed_table_s)}\n{mixed_table_s}\n'
          f'Список псевдослучайных слов:\n{random_words}\n\n'
          
          f'Сообщение для зашифровки:\n{message}\n'
          f'Сообщение в виде десятичных чисел:\n{message_10}\n\n'
          
          f'Зашифрованное сообщение:\n{encrypt_message}\n'
          f'Зашифрованное сообщение в виде десятичных чисел:\n{encrypt_message_10}\n'
          f'Время зашифровывания: {encrypt_time}\n\n'
          
          f'Расшифрованное сообщение:\n{decrypt_message}\n'
          f'Расшифрованное сообщение в виде десятичных чисел:\n{decrypt_message_10}\n'
          f'Время расшифровывания: {decrypt_time}\n\n'
          
          f'Сообщение расшифровано {"правильно" if decrypt_message == message else "не правильно"}!')


main()


def backpack(backpack_, target_value):
    # 197 + 132 + 90 + 56 + 28 + 14
    state = [(len(backpack_) - len(bin(i)[2:])) * '0' + bin(i)[2:] for i in range(2 ** len(backpack_))]

    target_element = ''

    for numb in state:
        current_value = 0
        for index, i in enumerate(numb):
            if i == '1':
                current_value += backpack_[index]
            if current_value > target_value:
                break
            if current_value == target_value:
                target_element = numb[::-1]
                break
        if current_value == target_value:
            break

    size_element = []
    for index, i in enumerate(target_element):
        if i == '1':
            size_element.append(backpack_[::-1][index])

    print(f'Вес всех вещей: {sum(backpack_)}')
    if current_value != target_value:
        print(f'Нельзя "собрать рюкзак" размером {target_value}\n')
    else:
        print(f'Размер рюкзака: {target_value}\n'
              f'Значение последовательности: {target_element}\n'
              f'Значение веса предметов: {size_element}\n')


target_value = 516
backpack_ = [14, 28, 56, 82, 90, 132, 197, 284, 341, 455]
backpack(backpack_, target_value)


def backpack_2():
    d = [103, 107, 211, 430, 863, 1716, 3449, 6907, 13807, 27610]
    n = 55205
    a = 7

    e = [(i * a) % n for i in d]
    print(f'Вес всех вещей: {sum(d)}\n'
          f'n = {n}\n'
          f'a = {a}\n'
          f'd = {d}\n'
          f'e = {e}\n')
    pass


backpack_2()
