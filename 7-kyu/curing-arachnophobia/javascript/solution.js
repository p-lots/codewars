const drawSpider = (legSize, bodySize, mouth, eye) => {
  const legType = { 1: "^ ^", 2: "/\\ /\\", 3: "/╲ ╱\\", 4: "╱╲ ╱╲" };
  const legs = legType[legSize].split(" ");
  const body = `${"(".repeat(bodySize)} ${")".repeat(bodySize)}`.split(" ");
  const numEyes = 2 ** bodySize;
  const eyes = eye.repeat(numEyes / 2);
  const spider = `${legs[0]}${body[0]}${eyes}${mouth}${eyes}${body[1]}${legs[1]}`;
  return spider;
};
