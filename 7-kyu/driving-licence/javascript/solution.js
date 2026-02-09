const driver = (data) => {
  const [ firstName, middleName, lastName, dob, sex ] = data;
  const [ day, month, year ] = dob.split("-");
  const parsedDate = new Date(`${year}-${month}-${day}`);
  
  // 1–5: The first five characters of the surname (padded with 9s if less than 5 characters)
  const paddedLastName = lastName.slice(0, 5).padEnd(5, "9").toUpperCase();
  
  // 6: The decade digit from the year of birth (e.g. for 1987 it would be 8)
  const decadeDigit = year[year.length - 2];
  
  // 7–8: The month of birth (7th character incremented by 5 if driver is female i.e. 51–62 instead of 01–12)
  const m = `${parsedDate.getMonth() + 1}`.padStart(2, "0");
  const monthDigits = sex === "F" ? `${Number(m[0]) + 5}${m[1]}` : m;
  
  // 9–10: The date within the month of birth
  const date = `${parsedDate.getDate()}`.padStart(2, "0");
  
  // 11: The year digit from the year of birth (e.g. for 1987 it would be 7)
  const yearDigit = year[year.length - 1];
  
  // 12–13: The initial letter of the first name and middle name, padded with a 9 if no middle name
  const initialName = `${firstName[0]}${middleName.length > 0 ? middleName[0] : "9"}`;
  
  // 14: Arbitrary digit – usually 9, but decremented to differentiate drivers with the first 13 characters in common. We will always use 9
  const arbitraryDigit = "9";
  
  // 15–16: Two computer check digits. We will always use "AA"
  const checkDigits = "AA";
  
  return `${paddedLastName}${decadeDigit}${monthDigits}${date}${yearDigit}${initialName}${arbitraryDigit}${checkDigits}`;
};
