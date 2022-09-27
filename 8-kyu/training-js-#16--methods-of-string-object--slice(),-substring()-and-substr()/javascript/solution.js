const cutIt = (arr) => {
  const minLength = Math.min(...arr.map(elem => elem.length));
  return arr.map(elem => elem.slice(0, minLength));
};
