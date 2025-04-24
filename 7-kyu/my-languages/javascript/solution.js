const myLanguages = results => Object.entries(results)
  .filter(([_, score]) => score >= 60)
  .sort((a, b) => b[1] - a[1])
  .map(([lang, _]) => lang);
