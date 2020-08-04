/**
 * @param {string} s
 * @return {boolean}
 */
var parentheses = {
    "(": ")",
    "{": "}",
    "[": "]"
};

var isValid = function (s) {
    var stack = [];

    for (var i = 0; i < s.length; i++) {
        if (s[i] === parentheses[stack[stack.length - 1]]) stack.pop();
        else stack.push(s[i]);
    }

    return stack.length === 0;
};