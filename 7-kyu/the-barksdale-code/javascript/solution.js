const decode = string => {
  const lookupTable = {"0": "5", "1": "9", "2": "8", "3": "7", "4": "6", "5": "0", "6": "4", "7": "3", "8": "2", "9": "1"};
  return string.split('').map(elem => lookupTable[elem]).join('');
}