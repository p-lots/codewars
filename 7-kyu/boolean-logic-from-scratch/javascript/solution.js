const or = (a, b) => {
  if (Boolean(a)) {
    return true;
  } else if (Boolean(b)) {
    return true;
  }
  return Boolean(a) && Boolean(b);
};

const xor = (a, b) => Boolean(a) !== Boolean(b);
