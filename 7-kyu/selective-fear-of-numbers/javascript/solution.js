const AmIAfraid = (day, num) => {
  const isAfraid = {
    Monday:    (n) => n === 12,
    Tuesday:   (n) => n > 95,
    Wednesday: (n) => n === 34,
    Thursday:  (n) => n === 0,
    Friday:    (n) => n % 2 === 0,
    Saturday:  (n) => n === 56,
    Sunday:    (n) => Math.abs(n) === 666
  };
  return isAfraid[day](num);
};
