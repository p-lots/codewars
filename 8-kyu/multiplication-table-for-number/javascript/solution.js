const multiTable = number => {
  let ret = [];
  for (let i = 1; i <= 10; i++) {
    ret.push(`${i} * ${number} = ${i * number}`);
  }
  return ret.join('\n');
}