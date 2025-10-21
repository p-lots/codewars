const lowercaseCount = str => {
  const regex = /[a-z]/g;
  const matches = str.match(regex);
  return matches?.length ?? 0;
};
