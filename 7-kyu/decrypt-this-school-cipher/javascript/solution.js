const decrypt = str => {
  let i = 0;
  let ret = "";
  while (i < str.length) {
    let ascii = "";
    if (str[i] == "'") {
      i++;
      while (str[i] != "'") {
        ascii += str[i];
        i++;
      }
      ret += String.fromCharCode(parseInt(ascii));
    } else {
      ret += str[i];
    }
    i++;
  }
  return ret.split("").reverse().join("");
}
