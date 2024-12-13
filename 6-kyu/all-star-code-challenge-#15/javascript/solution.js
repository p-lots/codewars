const rotate = str => Array.from({ length: str.length }, (_, idx) => str.slice(idx + 1) + str.slice(0, idx + 1));
