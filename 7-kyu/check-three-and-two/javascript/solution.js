const checkThreeAndTwo = array => {
  const count = (a, val) => a.filter(elem => elem === val).length;
  const aCount = count(array, "a");
  const bCount = count(array, "b");
  const cCount = count(array, "c");
  const checkThree = aCount === 3 || bCount === 3 || cCount === 3;
  const checkTwo = aCount === 2 || bCount === 2 || cCount === 2;
  return checkThree && checkTwo;
};
