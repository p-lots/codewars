const vertMirror = strng => strng.split('\n').map(elem => elem.split('').reverse().join('')).join('\n');

const horMirror = strng => strng.split('\n').reverse().join('\n');

const oper = (fct, s) => fct(s);