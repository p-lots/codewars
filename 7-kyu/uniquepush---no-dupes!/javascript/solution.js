//only push obj onto arr if it has a unique phoneNumber
const uniquePush = (arr, obj) => {
  for (const { name, phoneNumber } of arr) {
    if (!obj.phoneNumber || obj.phoneNumber === phoneNumber) {
      return false;
    }
  }
  arr.push(obj);
  return true;
};
