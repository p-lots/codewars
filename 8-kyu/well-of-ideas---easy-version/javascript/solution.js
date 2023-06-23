const well = (x) => {
  const good_count = x.filter(elem => elem === "good").length;
  if (good_count > 2) {
    return "I smell a series!";
  } else if (good_count >= 1) {
    return "Publish!";
  }
  return "Fail!";
};
