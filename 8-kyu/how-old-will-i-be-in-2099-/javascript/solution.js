const calculateAge = (birthYear, currentYear) => {
  const age = currentYear - birthYear;
  const yearWord = Math.abs(age) === 1 ? "year" : "years";
  let phrase = "";
  if (age > 0) {
    phrase = `You are ${age} ${yearWord} old.`;
  } else if (age < 0) {
    phrase = `You will be born in ${Math.abs(age)} ${yearWord}.`;
  } else {
    phrase = "You were born this very year!";
  }
  return phrase;
};
