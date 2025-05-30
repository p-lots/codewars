const sillycase = silly => {
  const midpoint = silly.length / 2 + silly.length % 2;
  return silly.slice(0, midpoint).toLowerCase() + silly.slice(midpoint).toUpperCase();
};
