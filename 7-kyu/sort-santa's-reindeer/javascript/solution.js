function sortReindeer(reindeerNames) {
  return reindeerNames.sort((a, b) =>{
    const aLastName = a.split(" ")[1];
    const bLastName = b.split(" ")[1];
    return aLastName.localeCompare(bLastName);
  });
}