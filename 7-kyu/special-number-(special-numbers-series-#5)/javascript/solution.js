const specialNumber = (n) => {
  const nStr = n.toString();
  return /^[012345]+$/g.test(nStr) ? "Special!!" : "NOT!!";
}