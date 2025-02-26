// return masked string
export const maskify = (cc: string): string => {
  if (cc.length <= 4) {
    return cc;
  }
  return "#".repeat(cc.length - 4) + cc.slice(-4);
}