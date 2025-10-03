export const flip = (dir: string, arr: number[]): number[] => dir === "R" ? arr.sort((a, b) => a - b) : arr.sort((a, b) => b - a);
