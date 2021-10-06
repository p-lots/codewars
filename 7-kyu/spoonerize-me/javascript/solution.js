const spoonerize = words => {
  let wordsSplit = words.split(" ");
  return `${wordsSplit[1][0]}${wordsSplit[0].slice(1)} ${wordsSplit[0][0]}${wordsSplit[1].slice(1)}`;
}