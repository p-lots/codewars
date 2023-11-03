const validParentheses = parenStr => {
  if (parenStr.length === 0) {
    return true;
  }
  const queue = [];
  let isValid = false;
  for (const ch of parenStr) {
    if (ch === "(") {
      queue.push(ch);
    } else if (ch === ")") {
      if (queue.length > 0 && queue[0] === "(") {
        isValid = true;
        queue.shift();
      } else {
        isValid = false;
        break;
      }
    }
  }
  return queue.length === 0 && isValid;
};
