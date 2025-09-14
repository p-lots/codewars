export const remove = (s: string): string => {
  return `${s.replace(/!/g, "")}!`;
};
