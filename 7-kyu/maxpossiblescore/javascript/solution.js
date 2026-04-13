const maxPossibleScore = (obj, arr) => Object.entries(obj).reduce((acc, [key, value]) => acc + (arr.includes(key) ? value * 2 : value), 0);
