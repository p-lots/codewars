const bigToSmall = arr => {  
  const flatArr = [].concat(...arr);
  return flatArr.sort((a, b) => b - a).join(">");
};
