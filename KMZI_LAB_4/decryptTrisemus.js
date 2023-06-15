const trisemusTable = [
    ['S', 'E', 'C', 'U', 'R'],
    ['I', 'T', 'Y', 'A', 'B'],
    ['D', 'F', 'G', 'H', 'J'],
    ['K', 'L', 'M', 'N', 'O'],
    ['P', 'Q', 'V', 'W', 'X'],
    ['Z', ' ', ',', '.', '\'']
];

function decryptTrisemus(message) {
    let encryptedMessage = '';
    for (let i = 0; i < message.length; i++) {
        let char = message[i];
        let row = -1;
        let col = -1;
        for (let j = 0; j < trisemusTable.length; j++) {
            for (let k = 0; k < trisemusTable[j].length; k++) {
                if (trisemusTable[j][k] === char) {
                    row = j;
                    col = k;
                    break;
                }
            }
            if (row !== -1 && col !== -1) {
                break;
            }
        }
        if (row === -1 || col === -1) {
            encryptedMessage += char;
        } else {
            let newRow = row;
            let newCol = col;
            if (newRow === 0) {
                newRow = 5;
            } else {
                newRow--;
            }
            encryptedMessage += trisemusTable[newRow][newCol];
        }
    }
    return encryptedMessage;
}

const fs = require('fs');

const decryptFilePath = 'decryptTrisemus.txt';
const outputFilePath = 'outputTrisemus.txt';

console.time('Decrypt Trisemus');

fs.readFile(outputFilePath, 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }
    const decipheredData = decryptTrisemus(data.toUpperCase());
    console.timeEnd('Decrypt Trisemus');
    fs.writeFile(decryptFilePath, decipheredData, (err) => {
        if (err) {
            console.error(err);
            return;
        }
        console.log(`Successfully ciphered data and saved to ${decryptFilePath}`);
    });
});