//These are your super secret characters you will use to make the password super secure
const superSecretChars = [['a', '@'],['s', '$'],['o', '0'], ['h', '5'], ['x', '*']];

const createSSP = (password) => {
  if (!password) {
    return "";
  }
  let ret = "";
  for (const ch of password) {
    let toAppend = "";
    for (const pair of superSecretChars) {
      if (ch.toLowerCase() === pair[0]) {
        toAppend = pair[1];
        break;
      } else {
        toAppend = ch;
      }
    }
    ret += toAppend;
  }
  return ret;
};
