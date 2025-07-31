const uglifyWord = s => {
  let uglyWord = "";
  let flag = true;
  for (let i = 0; i < s.length; i++) {
    if (/[a-z]/ig.test(s[i])) {
      if (flag) {
        uglyWord += s[i].toUpperCase();
      } else {
        uglyWord += s[i].toLowerCase();
      }
      flag = !flag;
    } else {
      uglyWord += s[i];
      flag = true;
    }
  }
  return uglyWord;
}
