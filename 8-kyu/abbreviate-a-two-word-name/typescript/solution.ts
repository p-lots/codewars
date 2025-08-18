export const abbrevName = (name: string): string => {
  const [first, last] = name.split(" ");
  const firstInitial = first[0];
  const lastInitial = last[0];
  return `${firstInitial.toUpperCase()}.${lastInitial.toUpperCase()}`;
};
