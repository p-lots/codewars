const arrayInfo = arr => {
  if (arr.length === 0) {
    return "Nothing in the array!";
  }
  const countOfIntegers = arr.filter(elem => Number.isInteger(elem)).length || null;
  const countOfFloats = arr.filter(elem => !Number.isInteger(elem) && Number.isFinite(elem)).length || null;
  const countOfStrings = arr.filter(elem => typeof elem === "string" && !/\s+/g.test(elem)).length || null;
  const countOfWhitespace = arr.filter(elem => typeof elem === "string" && /\s+/g.test(elem)).length || null;
  return [[arr.length], [countOfIntegers], [countOfFloats], [countOfStrings], [countOfWhitespace]];
};
