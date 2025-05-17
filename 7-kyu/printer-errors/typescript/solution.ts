export const printerError = (s: string): string => {
  const rgx = /[n-z]/g;
  const count = s.match(rgx)?.length ?? 0;
  return `${count}/${s.length}`;
};
