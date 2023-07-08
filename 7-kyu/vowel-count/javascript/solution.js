const getCount = str => {
  return [...str].filter((elem) => 'aeiou'.includes(elem.toLowerCase())).length;
};