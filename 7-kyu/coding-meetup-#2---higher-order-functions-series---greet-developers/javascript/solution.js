const greetDevelopers = (list) => {
  let ret = [];
  for (const obj of list) {
    let temp = obj;
    temp.greeting = `Hi ${obj.firstName}, what do you like the most about ${obj.language}?`;
    ret.push(temp);
  }
  return ret;
};
