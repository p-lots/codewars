const rateCalc = (hours, closeness) => {
  switch (closeness.toLowerCase()) {
      case "close friend":
      return hours * 25;
      case "friend":
      return hours * 50;
      case "acquaintance":
      return hours * 100;
      default:
      return hours * 125;
  }
}

const bearDollars = arr => {
  return arr.reduce((acc, elem) => acc + rateCalc(elem[0], elem[1]), 0);
}