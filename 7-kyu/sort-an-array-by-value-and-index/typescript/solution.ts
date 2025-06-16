export const sortByValueAndIndex = (array: number[]): number[] => array.map((n, i) => [n, n * (i + 1)]).sort((a, b) => a[1] - b[1]).map(n => n[0]);
