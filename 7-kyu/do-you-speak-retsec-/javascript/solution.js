const reverseByCenter = s => {
  const firstHalf = s.slice(0, Math.floor(s.length / 2));
  const secondHalf = s.slice(Math.ceil(s.length / 2));
  const middle = s.length % 2 === 1 ? s[Math.ceil(s.length / 2) - 1] : "";
  return `${secondHalf}${middle}${firstHalf}`;
};
