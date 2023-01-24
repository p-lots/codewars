const printerError = s => {
  let invalidCharCount = s.split("").reduce((acc, nxt) => acc + (nxt > "m" ? 1 : 0), 0);
  return `${invalidCharCount}/${s.length}`;
}