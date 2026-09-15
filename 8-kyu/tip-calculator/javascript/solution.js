const calculateTip = (amount, rating) => {
  const percentages = {
    terrible: 0,
    poor: 0.05,
    good: 0.1,
    great: 0.15,
    excellent: 0.2
  };
  const ratingLower = rating.toLowerCase();
  return percentages.hasOwnProperty(ratingLower) ? Math.ceil(amount * percentages[ratingLower]) : "Rating not recognised";
};
