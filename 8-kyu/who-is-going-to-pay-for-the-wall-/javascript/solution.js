const whoIsPaying = (name) => {
  if (name.length > 2) {
    return [name, name.slice(0, 2)];
  }
  return [name];
};
