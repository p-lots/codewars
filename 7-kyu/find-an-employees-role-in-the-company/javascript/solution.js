const findEmployeesRole = (name) => {
  const [firstName, lastName] = name.split(" ");
  const foundEmployee = employees.find(e => e.firstName === firstName && e.lastName === lastName);
  return foundEmployee?.role ?? "Does not work here!";
};
