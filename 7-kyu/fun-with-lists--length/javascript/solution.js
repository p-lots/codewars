const length = (head, len = 0) => {
  if (!head) {
    return len;
  }
  return length(head.next, len + 1);
}