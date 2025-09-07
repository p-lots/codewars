export const toCsvText = (array: number[][]): string => array.map(row => row.map(elem => elem.toString()).join(",")).join("\n");
