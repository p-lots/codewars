const convertCF = (num, scale="c") => {
  switch (scale) {
      case "f":
      return num * 9/5 + 32;
      case "c":
      return (num - 32) * 5/9;
      default:
      throw new Error();
  }
}