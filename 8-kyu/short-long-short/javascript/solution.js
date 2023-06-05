const solution = (a, b) => {
  const long = a.length > b.length ? a : b;
  const short = a.length < b.length ? a : b;
  return `${short}${long}${short}`;
};
