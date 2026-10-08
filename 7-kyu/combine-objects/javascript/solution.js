const combine = (...objs) => {
  let combined = {};
  for (const obj of objs) {
    for (const prop in obj) {
      if (!combined.hasOwnProperty(prop)) {
        combined[prop] = obj[prop];
      } else {
        combined[prop] += obj[prop];
      }
    }
  }
  return combined;
};
