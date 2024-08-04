export const bmi = (weight: number, height: number): string => {
  const calculatedBmi = weight / (height * height);
  if (calculatedBmi > 30.0) {
    return "Obese";
  }
  if (calculatedBmi > 25.0 && calculatedBmi <= 30.0) {
    return "Overweight";
  }
  if (calculatedBmi > 18.5 && calculatedBmi <= 25.0) {
    return "Normal";
  }
  return "Underweight";
};
