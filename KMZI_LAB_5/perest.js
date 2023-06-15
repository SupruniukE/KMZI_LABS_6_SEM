const fs = require('fs');

function encryptByRoutePermutation(text) {
    const textLength = text.length;
    const columns = 3;
    const rows = Math.ceil(textLength / columns);
    const matrix = new Array(rows).fill().map(() => new Array(columns).fill(''));
    let row = 0;
    let col = 0;
    let pos = 0
    for (let col = 0; col < columns; col++) {
        for (let row = 0; row < rows; row++) {
            matrix[row][col] = text[pos++];
            // if (row == 0) {
            //     console.log();
            // }
            // process.stdout.write(matrix[row][col]);
            // console.log('Row = ' + row + ', Column = ' + col + ', Symbol = ' + matrix[row][col]);
        }
    }

    for (let col = 0; col < columns; col++) {
        for (let row = 0; row < rows; row++) {
            if (row == 0) {
                console.log();
            }
            process.stdout.write(matrix[row][col]);
        }
    }

    console.log();
    let result = '';
    for (let row = 0; row < rows; row++) {
        // console.log('Row = ' + row);
        if (row % 2 == 1) {
            for (let col = 0; col < columns; col++) {
                result += matrix[row][col];
                // console.log('Row = ' + row + ', Column = ' + col + ', Symbol = ' + matrix[row][col]);
            }
        }
        else {
            for (let col = columns - 1; col >= 0; col--) {
                result += matrix[row][col];
                // console.log('Row = ' + row + ', Column = ' + j + ', Symbol = ' + matrix[row][j]);
            }
        }
    }

    return result;
}

function decryptByRoutePermutation(text) {
    const textLength = text.length;
    const columns = 3;
    const rows = Math.ceil(textLength / columns);
    const matrix = new Array(rows).fill().map(() => new Array(columns).fill(''));
    let row = 0;
    let col = 0;
    let pos = 0
    for (let row = 0; row < rows; row++) {
        for (let col = 0; col < columns; col++) {
            matrix[row][col] = text[pos++];
            // if (row == 0) {
            //     console.log();
            // }
            // process.stdout.write(matrix[row][col]);
            // console.log('Row = ' + row + ', Column = ' + col + ', Symbol = ' + matrix[row][col]);
        }
    }
    // for (let col = 0; col < columns; col++) {
    //     for (let row = 0; row < rows; row++) {
    //         matrix[row][col] = text[pos++];
    //         // if (row == 0) {
    //         //     console.log();
    //         // }
    //         // process.stdout.write(matrix[row][col]);
    //         // console.log('Row = ' + row + ', Column = ' + col + ', Symbol = ' + matrix[row][col]);
    //     }
    // }

    for (let col = 0; col < columns; col++) {
        for (let row = 0; row < rows; row++) {
            if (row == 0) {
                console.log();
            }
            process.stdout.write(matrix[row][col]);
        }
    }
    console.log();
    const newMatrix = new Array(rows).fill().map(() => new Array(columns).fill(''));
    
    for (let row = rows - 1; row >= 0; row--) {
        // console.log('Row = ' + row);
        if (row % 2 == 1) {
            for (let col = 0; col < columns; col++) {
                newMatrix[row][col] += matrix[row][col];
                // process.stdout.write(matrix[j][i]);
                // console.log('Row = ' + row + ', Column = ' + col + ', Symbol = ' + matrix[row][col]);
            }
        }
        else {
            for (let col = columns - 1, ncol = 0; col >= 0; col--, ncol++) {
                newMatrix[row][ncol] += matrix[row][col];
                // process.stdout.write(matrix[j][i]);
                // console.log('Row = ' + row + ', Column = ' + j + ', Symbol = ' + matrix[row][j]);
            }
        }
    }
    let result = '';
    for (let col = 0; col < columns; col++) {
        for (let row = 0; row < rows; row++) {
            result += newMatrix[row][col];
        }
    }
    return result;
}

fs.readFile('input.txt', 'utf8', (err, data) => {
    if (err) throw err;
    fs.writeFile('output.txt', encryptByRoutePermutation(data), (err) => {
        if (err) throw err;
        fs.readFile('output.txt', 'utf8', (err, data) => {
            if (err) throw err;
            fs.writeFile('decrypt.txt', decryptByRoutePermutation(data), (err) => {
                if (err) throw err;
            });
        });
    });
});