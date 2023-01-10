const solve = s => Math.max(...(s.split(/[^aeiou]+/).map(elem => elem.length)));
