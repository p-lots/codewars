const colourAssociation = array => {
  let ret = [];
  for (const [color, assoc] of array) {
    let temp = {};
    temp[color] = assoc;
    ret.push(temp);
  }
  return ret;
}