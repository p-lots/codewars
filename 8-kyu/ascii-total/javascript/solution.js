const uniTotal = string => [...string].reduce((acc, nxt) => acc + nxt.charCodeAt(0), 0);
