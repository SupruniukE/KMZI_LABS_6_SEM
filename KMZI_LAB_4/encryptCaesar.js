const fs = require('fs');

const a = 5;
const b = 7;

const inputFilePath = 'inputCaesar.txt';
const outputFilePath = 'outputCaesar.txt';

const alphabet = 'abcdefghijklmnopqrstuvwxyz1234567890-=!@#$%^&*()_+ ';

const cipher = (char) => {
  const index = alphabet.indexOf(char);
  if (index === -1) {
    return char;
  }
  const newIndex = (a * index + b) % alphabet.length;
  const newChar = alphabet[newIndex];
  return newChar;
};

console.time('Encrypt Caesar');

fs.readFile(inputFilePath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  const cipheredData = data.split('').map(cipher).join('');
  console.timeEnd('Encrypt Caesar');
  fs.writeFile(outputFilePath, cipheredData, (err) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(`Successfully ciphered data and saved to ${outputFilePath}`);
  });
});