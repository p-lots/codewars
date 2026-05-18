const sentencify = words => {
  const joined = words.join(" ");
  return joined[0].toUpperCase() + joined.slice(1) + ".";
};
