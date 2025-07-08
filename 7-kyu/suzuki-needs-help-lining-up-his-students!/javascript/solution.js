const lineupStudents = students => {
  return students.split(" ").sort((a, b) => {
    if (a.length === b.length) {
      return b.localeCompare(a);
    }
    return b.length - a.length;
  });
};
