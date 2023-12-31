readInput = require('../utils.js');

const INPUT = readInput('input.txt');

const cache = {}

function countPermutations(damage, report) {
    if (damage + ' ' + report.toString() in cache) {
        return cache[damage + ' ' + report.toString()];
    }

    if (damage.length < report.reduce((a, b) => a + b, 0) + report.length - 1) {
        cache[damage + ' ' + report.toString()] = 0
        return 0;
    }

    if (report.length == 0) {
        let result = damage.includes('#') ? 0 : 1;
        cache[damage + ' ' + report.toString()] = result;
        return result;
    }

    let valid = !damage.slice(0, report[0]).includes('.');
    
    let sum = 0;

    // take
    if (valid && damage[report[0]] != '#') {
        sum += countPermutations(damage.slice(report[0] + 1), report.slice(1));
    }

    // skip
    if (damage[0] != '#') {
        sum += countPermutations(damage.slice(1), report);
    }

    cache[damage + ' ' + report.toString()] = sum;
    return sum;  
}


function part1(input) {
    let total = 0;
    for( const line of input.split('\n') ) {
        let [damage, report] = line.split(' ');
        report = report.split(',').map(x => Number(x));
        let res = countPermutations(damage, report);
        total += res;
    }
    return total;
}

console.log(part1(INPUT));


function part2(input) {
    let total = 0;
    const repeat = (arr, n) => [].concat(...Array(n).fill(arr));

    for( const line of input.split('\n') ) {
        let [damage, report] = line.split(' ');

        // unfold the input
        damage = ((damage + '?').repeat(5)).slice(0, -1);
        report = report.split(',').map(x => Number(x));
        report = repeat(report, 5);

        let res = countPermutations(damage, report);
        total += res;
    }
    return total;
}

console.log(part2(INPUT));
