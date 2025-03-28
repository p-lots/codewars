const initializeNames = name => {
  const nameSplit = name.split(" ");
  switch (nameSplit.length) {
      case 0:
      return "";
      case 1:
      case 2:
      return name;
      default:
      const middleInitials = nameSplit.slice(1, -1).map(n => `${n[0]}. `).join("");
      return `${nameSplit[0]} ${middleInitials}${nameSplit[nameSplit.length - 1]}`;
  }
};
