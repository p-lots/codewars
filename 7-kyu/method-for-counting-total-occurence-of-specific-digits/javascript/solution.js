function List() {
  this.countSpecDigits = function(integersList, digitsList) {
    const countDigits = (n, digit) => n.toString().split("").filter(elem => parseInt(elem) === digit).length;
    let ret = [];
    for (const digit of digitsList) {
      let count = 0;
      for (const integer of integersList) {
        count += countDigits(integer, digit);
      }
      ret.push([digit, count]);
    }
    return ret;
  };
}
