const bucketOf = str => {
  const slimeTest = /(i don't know)|(slime)/gi.test(str);
  const waterTest = /(water)|(wet)|(wash)/gi.test(str);
  let contents = "air";
  if (slimeTest) {
    if (waterTest) {
      contents = "sludge";
    } else {
      contents = "slime";
    }
  }
  else if (waterTest) {
    contents = "water";
  }
  return contents;
};
