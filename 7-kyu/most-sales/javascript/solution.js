const top3 = (products, amounts, prices) => {
  const topProducts = products.map((product, idx) => {
    const obj = {};
    obj.name = product;
    obj.revenue = amounts[idx] * prices[idx];
    return obj;
  }).sort((a, b) => b.revenue - a.revenue).map(p => p.name).slice(0, 3);
  return topProducts;
};
