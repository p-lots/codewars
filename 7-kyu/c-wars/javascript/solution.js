const initials = name => {
  const capitalize = str => `${str[0].toUpperCase()}${str.slice(1).toLowerCase()}`;
  const nameSplit = name.split(" ");
  const nameInitialized = nameSplit
    .map((init, idx, arr) => idx < arr.length - 1 ? init[0].toUpperCase() : capitalize(init));
  return nameInitialized.join(".");
};
