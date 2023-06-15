const fs = require('fs');

const a = 5;
const b = 7;

const decryptFilePath = 'decryptCaesar.txt';
const outputFilePath = 'outputCaesar.txt';

const alphabet = 'abcdefghijklmnopqrstuvwxyz1234567890-=!@#$%^&*()_+ ';

const modInverse = (a, m) => {
    a = ((a % m) + m) % m;
    for (let x = 1; x < m; x++) {
        if ((a * x) % m === 1) {
            return x;
        }
    }
    return 1;
};

const decipher = (char) => {
    const index = alphabet.indexOf(char);
    if (index === -1) {
        return char;
    }
    let newIndex = index - b;
    while (newIndex < 0) {
        newIndex += alphabet.length;
    }
    newIndex = (newIndex * modInverse(a, alphabet.length)) % alphabet.length;
    const newChar = alphabet[newIndex];
    return newChar;
};

console.time('Decrypt Caesar');

fs.readFile(outputFilePath, 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }
    const decipheredData = data.split('').map(decipher).join('');
    console.timeEnd('Decrypt Caesar');
    fs.writeFile(decryptFilePath, decipheredData, (err) => {
        if (err) {
          console.error(err);
          return;
        }
        console.log(`Successfully deciphered data and saved to ${decryptFilePath}`);
      });
});
