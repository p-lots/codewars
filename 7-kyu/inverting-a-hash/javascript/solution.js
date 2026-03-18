const invertHash = hash => Object.entries(hash).reduce((obj, [key, val]) => { obj[val] = key; return obj; }, {});
