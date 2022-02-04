const bmi = (weight, height) => {
  const calculatedBmi = weight / (height * height);
  if (calculatedBmi <= 18.5) {
    return "Underweight";
  } else if (calculatedBmi <= 25.0) {
    return "Normal";
  } else if (calculatedBmi <= 30.0) {
    return "Overweight";
  }
  return "Obese";
};