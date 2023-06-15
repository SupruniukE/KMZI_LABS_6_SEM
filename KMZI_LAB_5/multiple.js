const fs = require('fs');

function encryptMultiplePermutation(plaintext, keyword1, keyword2) {
    let ciphertext = '';
    for (let chunk = 0; chunk < plaintext.length / (keyword1.length * keyword2.length); chunk++) {
        let matrix = [];
        for (let i = 0; i < keyword2.length; i++) {
            matrix.push([]);
            for (let j = 0; j < keyword1.length; j++) {
                matrix[i][j] = i * keyword1.length + j < Math.min((keyword1.length * keyword2.length), plaintext.length - chunk * keyword1.length * keyword2.length) ?
                    plaintext[chunk * keyword1.length * keyword2.length + i * keyword1.length + j] : ' ';
            }
        }
        for (let i = 0; i < matrix.length; i++) {
            console.log(matrix[i]);
        }
        console.log();
        matrix = [...keyword2].map((value, index) => ({ index: index, letter: value }))
            .sort((a, b) => a.letter === b.letter ? 0 : (a.letter < b.letter ? -1 : 1))
            .map((value, index) => ({ index: value.index, array: matrix[index] }))
            .sort((a, b) => a.index === b.index ? 0 : (a.index < b.index ? -1 : 1))
            .map(value => value.array);
        for (let i = 0; i < matrix.length; i++) {
            console.log(matrix[i]);
        }
        console.log();
        matrix = [...keyword1].map((value, index) => ({ index: index, letter: value }))
            .sort((a, b) => a.letter === b.letter ? 0 : (a.letter < b.letter ? -1 : 1))
            .map((value, index) => ({ index: value.index, array: matrix.map(row => row[index]) }))
            .sort((a, b) => a.index === b.index ? 0 : (a.index < b.index ? -1 : 1))
            .map(value => value.array);
        for (let i = 0; i < matrix.length; i++) {
            console.log(matrix[i]);
        }
        console.log();
        for (let i = 0; i < keyword2.length; i++) {
            for (let j = 0; j < keyword1.length; j++) {
                ciphertext += matrix[i][j];
            }
        }
    }
    return ciphertext;
}

function decryptMultiplePermutation(ciphertext, keyword1, keyword2) {
    let plaintext = '';
    for (let chunk = 0; chunk < ciphertext.length / (keyword1.length * keyword2.length); chunk++) {
        let matrix = [];
        for (let i = 0; i < keyword2.length; i++) {
            matrix.push([]);
            for (let j = 0; j < keyword1.length; j++) {
                matrix[i][j] = ciphertext[chunk * keyword1.length * keyword2.length + i * keyword1.length + j]
            }
        }
        matrix = [...keyword1].map((value, index) => ({ letter: value, index: index }))
            .map((value, index) => ({ letter: value.letter, array: matrix[index] }))
            .sort((a, b) => a.letter === b.letter ? 0 : (a.letter < b.letter ? -1 : 1))
            .map(value => value.array);
        matrix = [...keyword2].map((value, index) => ({ letter: value, index: index }))
            .map((value, index) => ({ letter: value.letter, array: matrix.map(row => row[index]) }))
            .sort((a, b) => a.letter === b.letter ? 0 : (a.letter < b.letter ? -1 : 1))
            .map(value => value.array);
        for (let i = 0; i < keyword2.length; i++) {
            for (let j = 0; j < keyword1.length; j++) {
                plaintext += matrix[i][j];
            }
        }
    }
    return plaintext;
}

fs.readFile('inputM.txt', 'utf8', (err, data) => {
    if (err) throw err;
    fs.writeFile('outputM.txt', encryptMultiplePermutation(data, 'abc', 'cba'), (err) => {
        if (err) throw err;
        fs.readFile('outputM.txt', 'utf8', (err, data) => {
            if (err) throw err;
            fs.writeFile('decryptM.txt', decryptMultiplePermutation(data, 'abc', 'cba'), (err) => {
                if (err) throw err;
            });
        });
    });
});