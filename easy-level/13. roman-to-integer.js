/**
 * @param {string} s
 * @return {number}
 */

var symbols = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

var romanToInt = function (s) {
    var str = s.split("").reverse();
    str.unshift(0);

    return str.reduce((acc, val, index) =>
        acc + (symbols[val] * (index - 1 === 0 ? 1 : symbols[str[index - 1]] <= symbols[val] ? 1 : -1)));
};