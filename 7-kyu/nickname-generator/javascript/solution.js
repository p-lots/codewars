const nicknameGenerator = (name) => {
  if (name.length <= 3) { 
    return "Error: Name too short";
  }
  const sliceLen = "aeiou".includes(name[2]) ? 4 : 3;
  return name.slice(0, sliceLen);
};
