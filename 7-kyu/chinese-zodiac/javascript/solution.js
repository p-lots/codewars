const chineseZodiac = year => {
  const elemYear = Math.floor((year - 1924) / 2) % 5;
  return `${elements[elemYear]} ${animals[(year - 1924) % 12]}`;
};
