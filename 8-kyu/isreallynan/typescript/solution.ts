export const isReallyNaN = (val: any): boolean => {
  // return isNaN(val);  // wasn't working as planned :-(
  return val !== val;
};
