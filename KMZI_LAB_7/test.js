// Подключаем модуль crypto
const crypto = require('crypto');

// Задаем ключ и алгоритм шифрования
const key = 'qwertyuiopasdfghjklzxcvb';
const algorithm = 'des-ede3';

// Функция для шифрования слова
function encrypt(word) {
  // Создаем объект шифрования с заданным ключом и алгоритмом
  const cipher = crypto.createCipheriv(algorithm, key, null);
  // Шифруем слово и возвращаем результат в формате base64
  let encrypted = cipher.update(word, 'utf8', 'base64');
  encrypted += cipher.final('base64');
  return encrypted;
}

// Функция для подсчета количества изменяющихся символов в зашифрованном слове по отношению к исходному
function countChanges(original, encrypted) {
  // Преобразуем зашифрованное слово в бинарный формат
  let binary = Buffer.from(encrypted, 'base64').toString('binary');
  // Инициализируем счетчик изменений
  let changes = 0;
  // Проходим по каждому символу исходного и зашифрованного слова
  for (let i = 0; i < original.length; i++) {
    // Получаем бинарное представление символов
    let originalChar = original.charCodeAt(i).toString(2);
    let encryptedChar = binary.charCodeAt(i).toString(2);
    // Дополняем нулями до восьми битов
    originalChar = originalChar.padStart(8, '0');
    encryptedChar = encryptedChar.padStart(8, '0');
    // Сравниваем каждый бит и увеличиваем счетчик, если они различаются
    for (let j = 0; j < 8; j++) {
      if (originalChar[j] !== encryptedChar[j]) {
        changes++;
      }
    }
  }
  // Возвращаем счетчик изменений
  return changes;
}

// Функция для пошагового анализа лавинного эффекта
function analyzeAvalanche(word) {
  // Шифруем исходное слово
  let originalEncrypted = encrypt(word);
  // Выводим результат на экран
  console.log(`Исходное слово: ${word}`);
  console.log(`Зашифрованное слово: ${originalEncrypted}`);
  console.log(`Количество изменяющихся символов: ${countChanges(word, originalEncrypted)}`);
  console.log('--------------------------');
  // Проходим по каждому символу исходного слова
  for (let i = 0; i < word.length; i++) {
    // Создаем копию исходного слова
    let modifiedWord = word.slice();
    // Меняем текущий символ на случайный из алфавита
    let alphabet = 'abcdefghijklmnopqrstuvwxyz';
    let randomChar = alphabet[Math.floor(Math.random() * alphabet.length)];
    modifiedWord = modifiedWord.substr(0, i) + randomChar + modifiedWord.substr(i + 1);
    // Шифруем измененное слово
    let modifiedEncrypted = encrypt(modifiedWord);
    // Выводим результат на экран
    console.log(`Измененное слово: ${modifiedWord}`);
    console.log(`Зашифрованное слово: ${modifiedEncrypted}`);
    console.log(`Количество изменяющихся символов: ${countChanges(modifiedWord, modifiedEncrypted)}`);
    console.log('--------------------------');
  }
}

// Тестируем функцию анализа лавинного эффекта на примере слова "hello"
analyzeAvalanche('hello');