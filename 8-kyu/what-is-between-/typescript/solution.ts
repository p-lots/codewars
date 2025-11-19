export const between = (a: number, b: number): number[] => Array.from({ length: b - a + 1 }, (_, idx) => idx + a);
