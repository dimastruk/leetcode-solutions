/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function (strs) {
    if (strs.length === 0) return "";
    if (strs.some(str => str === "")) return "";
  
    var characters = strs.map(str => str.split("").shift());
  
    var isCommonPrefix = characters.every(character => character === characters[0]);
    
    var result = isCommonPrefix ? characters[0] : "";
    var nextPrefix = isCommonPrefix ? longestCommonPrefix(strs.map(str => str.substring(1))) : "";
  
    return result + nextPrefix;
  };