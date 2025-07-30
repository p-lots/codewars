export const twoArePositive = (a: number, b: number, c: number): boolean => [a, b, c].filter(num => num > 0).length === 2;
