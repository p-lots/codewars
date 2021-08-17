function range(startNum, endNum)   
{  
  if (startNum === endNum || !(startNum + 1 < endNum)) {
    return [];
  }
  let ret = [];
  for (let i = startNum + 1; i < endNum; i++) {
    ret.push(i);
  }
  return ret;
};  
  
