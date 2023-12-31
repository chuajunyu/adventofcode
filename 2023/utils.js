const fs = require('fs');

function readInput(inputPath) {
    return fs.readFileSync(inputPath, 'utf8');
}

module.exports = readInput;
