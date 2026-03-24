const missingWord = (nums, str) => {
  const preparedStr = str.replace(/ /g, "");
  if (nums.some(givenIdx => givenIdx >= preparedStr.length)) {
    return "No mission today";
  }
  return nums.sort((a, b) => a - b).map(givenIdx => preparedStr[givenIdx]).join("").toLowerCase();
};
