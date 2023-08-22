const isValid = query => {
  const querySplit = query.split(" ");
  const queryFilter = querySplit.filter(elem => elem.includes(":"));
  return queryFilter.every(elem => FILTERS.includes(elem.split(":")[0]));
};
