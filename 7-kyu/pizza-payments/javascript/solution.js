const michaelPays = pizzaCost => {
  if (pizzaCost < 5) {
    return Number(pizzaCost.toFixed(2));
  }
  const katePays = Math.min(pizzaCost * (1 / 3), 10);
  const michaelPays = Math.round((pizzaCost - katePays) * 100) / 100;
  return michaelPays;
};
