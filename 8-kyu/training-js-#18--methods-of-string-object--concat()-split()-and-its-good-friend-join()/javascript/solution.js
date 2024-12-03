const splitAndMerge = (string, separator) => {
  const stringJoined = string.split(" ")
    .map(word => word.split("").join(separator))
    .join(" ");
  return stringJoined;
};
