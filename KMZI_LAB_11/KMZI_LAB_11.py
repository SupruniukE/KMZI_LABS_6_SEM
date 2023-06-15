def expansion_to_multiplicity_of_512(message_binary):
    if len(message_binary) % 512 < 448 and len(message_binary) % 512 != 0:
        extended_block = '1' + (448 - len(message_binary) % 512 - 1) * '0' \
                         + (64 - len(bin(len(message_binary))[2:])) * '0' + bin(len(message_binary))[2:]
    elif 448 < len(message_binary) % 512 < 512:
        extended_block = '1' + (512 - 1 - len(message_binary) % 512) * '0' \
                         + 448 * '0' + (64 - len(bin(len(message_binary))[2:])) * '0' + bin(len(message_binary))[2:]
    else:
        extended_block = '1' + 447 * '0' + (64 - len(bin(len(message_binary))[2:])) * '0' + bin(len(message_binary))[2:]
    extended_message = message_binary + extended_block
    return extended_message


def split_into_blocks(block, size_blocks):
    return [block[i * size_blocks: (i + 1) * size_blocks] for i in range(len(block) // size_blocks)]


message = 'Savul Diana Valerievna'
print(f'Сообщение для расширения: {message}')
print(f'Коды символов:')
for i in message:
    print(f'Символ {i}: {(8 - len(bin(ord(i))[2:])) * "0" + bin(ord(i))[2:]}')
message_2 = ''.join([(8 - len(bin(ord(i))[2:])) * '0' + bin(ord(i))[2:] for i in message])
message_2_len = bin(len(message_2))[2:]
message_extended = expansion_to_multiplicity_of_512(message_2)
message_16_32 = split_into_blocks(message_extended, 32)
print(f'Сообщение в ASCII: {message_2}\n'
      f'Длина сообщения в ASCII: {len(message_2)}\n'
      f'Двоичное представление длины сообщения в ASCII: {message_2_len}\n'
      f'Длина двоичного представления длины сообщения в ASCII: {len(message_2_len)}\n'
      f'Расширенное сообщение: {message_extended}\n'
      f'Длина расширенного сообщения: {len(message_extended)}\n'
      f'Расширенное сообщение, разбитое на 16 32-битных блока:')
for i in message_16_32:
    print(i)
