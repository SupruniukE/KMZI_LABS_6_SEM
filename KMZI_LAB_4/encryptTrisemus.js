const trisemusTable = [
    ['S', 'E', 'C', 'U', 'R'],
    ['I', 'T', 'Y', 'A', 'B'],
    ['D', 'F', 'G', 'H', 'J'],
    ['K', 'L', 'M', 'N', 'O'],
    ['P', 'Q', 'V', 'W', 'X'],
    ['Z', ' ', ',', '.', '\'']
];

function encryptTrisemus(message) {
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
            if (newRow === 5) {
                newRow = 0;
            } else {
                newRow++;
            }
            encryptedMessage += trisemusTable[newRow][newCol];
        }
    }
    return encryptedMessage;
}


const fs = require('fs');

const inputFilePath = 'inputTrisemus.txt';
const outputFilePath = 'outputTrisemus.txt';

console.time('Encrypt Trisemus');

fs.readFile(inputFilePath, 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }
    const cipheredData = encryptTrisemus(data.toUpperCase());
    console.timeEnd('Encrypt Trisemus');
    fs.writeFile(outputFilePath, cipheredData, (err) => {
        if (err) {
            console.error(err);
            return;
        }
        console.log(`Successfully ciphered data and saved to ${outputFilePath}`);
    });
});