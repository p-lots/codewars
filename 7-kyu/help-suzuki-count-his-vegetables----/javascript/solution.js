const countVegetables = deliveries => {
  const validVeggies = ["cabbage", "carrot", "celery",
                        "cucumber", "mushroom", "onion",
                        "pepper", "potato", "tofu", "turnip"];
  const veggieMap = new Map();
  const splitDeliveries = deliveries.split(" ");
  for (const item of splitDeliveries) {
    if (validVeggies.includes(item)) {
      if (veggieMap.has(item)) {
        const currVegCount = veggieMap.get(item);
        veggieMap.set(item, currVegCount + 1);
      } else {
        veggieMap.set(item, 1);
      }
    }
  }
  const veggieCounts = [];
  for (const [veg, vCount] of veggieMap.entries()) {
    veggieCounts.push([vCount, veg]);
  }
  const vegSorted = veggieCounts.sort((a, b) => {
    if (a[0] === b[0]) {
      return b[1].localeCompare(a[1]);
    }
    return b[0] - a[0];
  });
  return vegSorted;
};
