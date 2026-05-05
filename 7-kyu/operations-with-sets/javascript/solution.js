const process2Arrays = (arr1, arr2) => {
  const intersection = arr1.filter(n => arr2.includes(n)).length;
  const diff = arr1.filter(n => !arr2.includes(n)).length + arr2.filter(n => !arr1.includes(n)).length;
  const arr1Only = arr1.length - arr1.filter(n => arr2.includes(n)).length;
  const arr2Only = arr2.length - arr2.filter(n => arr1.includes(n)).length;
  return [intersection, diff, arr1Only, arr2Only];
};