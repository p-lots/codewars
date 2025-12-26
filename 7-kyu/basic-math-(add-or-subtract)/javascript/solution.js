const calculate = str => {
  const replaced = str.replace(/plus/g, "+").replace(/minus/g, "-");
  const digits = replaced.split(/[+-]/g);
  const operations = replaced.split(/(?:\d+)/).filter(Boolean);
  let result = Number(digits[0]);
  digits.shift();
  for (const oper of operations) {
    if (oper === "+") {
      result += Number(digits[0]);
    } else if (oper === "-") {
      result -= Number(digits[0]);
    }
    digits.shift();
  }
  return `${result}`;
};
