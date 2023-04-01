const strCount = (str, letter) => [...str].reduce((acc, nxt) => acc + (nxt === letter ? 1 : 0), 0);
