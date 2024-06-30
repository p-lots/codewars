const outed = (meet, boss) => {
  let sum = 0;
  for (const [employee, happiness] of Object.entries(meet)) {
    if (employee === boss) {
      sum += 2 * happiness;
    } else {
      sum += happiness;
    }
  }
  const mean = sum / Object.keys(meet).length;
  return mean <= 5 ? "Get Out Now!" : "Nice Work Champ!";
};
