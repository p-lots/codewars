export const shortLongShort = (a: string, b: string): string => {
  const short = a.length < b.length ? a : b;
  const long = a.length > b.length ? a : b;
  return `${short}${long}${short}`;
};
