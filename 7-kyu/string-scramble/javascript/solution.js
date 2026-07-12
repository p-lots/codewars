const scramble = (str, arr) => {
  let scrambled = str.split("");
  for (let i = 0; i < arr.length; i++) {
    scrambled[arr[i]] = str[i];
  }
  return scrambled.join("");
};