function last(x){
  return x.split(" ").sort((lhs, rhs) => {
    if (lhs[lhs.length - 1] > rhs[rhs.length - 1]) {
      return 1;
    } else if (lhs[lhs.length - 1] < rhs[rhs.length - 1]) {
      return -1;
    }
    return 0;
  });
}
