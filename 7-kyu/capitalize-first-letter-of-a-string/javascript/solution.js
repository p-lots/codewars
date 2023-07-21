String.prototype.capitalize = function() {
  let firstChar = this.slice(0, 1);
  if (firstChar.match(/[a-z]/)) {
    firstChar = firstChar.replace(/[a-z]/, function(match, ...args) {
      const lookup = {"a": "A", "b": "B", "c": "C", "d": "D", "e": "E",
                      "f": "F", "g": "G", "h": "H", "i": "I", "j": "J",
                      "k": "K", "l": "L", "m": "M", "n": "N", "o": "O",
                      "p": "P", "q": "Q", "r": "R", "s": "S", "t": "T",
                      "u": "U", "v": "V", "w": "W", "x": "X", "y": "Y",
                      "z": "Z"};
      return lookup[match];
    });
  }
  return `${firstChar}${this.slice(1)}`;
}
