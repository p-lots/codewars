const swapVowelCase = str => {
  const vowels = ['a', 'e', 'i', 'o', 'u'];
  return [...str].map((elem) => vowels.includes(elem.toLowerCase()) ? elem === elem.toLowerCase() ? elem.toUpperCase() : elem.toLowerCase() : elem).join('');
};
