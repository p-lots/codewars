const discoverOriginalPrice = (discountedPrice, salePercentage) => {
  const originalPrice = discountedPrice / (1 - salePercentage / 100);
  return Math.round(originalPrice * 100) / 100;
};
