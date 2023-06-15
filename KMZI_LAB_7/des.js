const crypto = require('crypto');

function encryptText(text, key) {
  const cipher = crypto.createCipheriv('des-ede3', key, null);
  let encrypted = cipher.update(text, 'utf8', 'base64');
  encrypted += cipher.final('base64');
  return encrypted;
}

function decryptText(encryptedText, key) {
  const decipher = crypto.createDecipheriv('des-ede3', key, null);
  let decrypted = decipher.update(encryptedText, 'base64', 'utf8');
  decrypted += decipher.final('utf8');
  return decrypted;
}

let text = 'Hello World!';
let key = 'qwertyuiopasdfghjklzxcvb';

console.log('Start')

console.time('encrypt');
let encryptedText = encryptText(text, key);
console.timeEnd('encrypt');
console.log(`Encrypted Text: ${encryptedText}`);

console.time('decrypt');
const decryptedText = decryptText(encryptedText, key);
console.timeEnd('decrypt');
console.log(`Decrypted Text: ${decryptedText}`);

console.log(text = 'abcdefg');
encryptedText = encryptText(text, key);
console.log(`Encrypted Text: ${encryptedText}`);

console.log(text = 'bbcdefg');
encryptedText = encryptText(text, key);
console.log(`Encrypted Text: ${encryptedText}`);

console.log(text = 'cbcdefg');
encryptedText = encryptText(text, key);
console.log(`Encrypted Text: ${encryptedText}`);