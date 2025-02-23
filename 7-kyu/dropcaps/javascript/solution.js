const dropCap = n => {
  const capitalize = match => {
    if (match.length > 2) {
      return match[0].toUpperCase() + match.slice(1).toLowerCase();
    }
    return match;
  };
  return n.replace(/\w+/gi, capitalize);
}