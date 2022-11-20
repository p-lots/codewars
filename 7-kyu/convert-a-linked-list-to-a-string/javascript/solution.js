const stringify = (list) => {
  if (list === null) {
    return "null";
  }
  let nxt = list.next;
  let ret = [list.data];
  while (nxt !== null) {
    ret.push(nxt.data);
    nxt = nxt.next;
  }
  ret.push("null");
  return ret.join(" -> ")
};
