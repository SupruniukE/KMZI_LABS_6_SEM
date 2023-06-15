import random


# секретная лазейка для прошлой лабы

def IsPrimitiveRoot(number, p):
    remains = set([(number ** i) % p for i in range(1, p)])
    return len(remains) == p - 1


def GenerateMainComponents(p):
    for i in range(2, p):
        if IsPrimitiveRoot(i, p):
            g = i
            break

    x = int(random.random() * (p - 1))
    y = (g ** x) % p

    public_key = p, g, y
    private_key = p, g, x
    k = int(random.random() * (p - 1))
    return public_key, private_key, k


def Encrypt(message, public_key, k):
    p, g, y = public_key
    M = [ord(i) for i in message]

    encrypt_message = []
    for i in M:
        encrypt_message.append(((g ** k) % p, (y ** k * i) % p))
    return encrypt_message


def Decrypt(encrypt_message, private_key, k):
    p, g, x = private_key

    decrypt_message = []
    for a_b in encrypt_message:
        decrypt_message.append(chr((a_b[1] * (a_b[0] ** (p - x - 1))) % p))
    return ''.join(decrypt_message)


def ELGamal(message, p=None):
    if p is None or p > 200:
        p = 191

    message_10 = [ord(i) for i in message]

    public_key, private_key, k = GenerateMainComponents(p)
    encrypt_message = Encrypt(message, public_key, k)
    decrypt_message = Decrypt(encrypt_message, private_key, k)

    print(f'----- Входная информация -----\n'
          f'Сообщение: {message}\n'
          f'Сообщение(10): {message_10}\n'
          f'p = {p}\n'
          f'----- Ключи -----\n'
          f'Открытый ключ: {public_key}\n'
          f'Закрытый ключ: {private_key}\n'
          f'----- Зашифровывание -----\n'
          f'Открытый ключ: {public_key}\n'
          f'k = {k}\n'
          f'Зашифрованное сообщение: {encrypt_message}\n'
          f'----- Расшифровывание -----\n'
          f'Закрытый ключ: {private_key}\n'
          f'Расшифрованное сообщение: {decrypt_message}\n'
          f'----- Успешность расшифровывания -----\n'
          f'Сообщение расшифровано {"правильно" if message == decrypt_message else "неправильно"}')
