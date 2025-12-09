function highestAge(group1, group2) {
  const combinedGroup = group1.concat(group2);
  const mergedGroup = [];
  for (const person of combinedGroup) {
    if (!mergedGroup.some(p => p.name === person.name)) {
      mergedGroup.push(person);
      continue;
    }
    for (const merged of mergedGroup) {
      if (person.name === merged.name) {
        merged.age += person.age;
      }
    }
  }
  const sorted = mergedGroup.sort((a, b) => {
    if (a.age > b.age) {
      return -1;
    } else if (a.age < b.age) {
      return 1;
    }
    return a.name.localeCompare(b.name);
  });
  return sorted[0].name;
}