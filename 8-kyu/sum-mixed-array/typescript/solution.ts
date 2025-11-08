export const sumMix = (x: any[]): number => x.map(n => typeof n === "number" ? n : Number(n)).reduce((acc, nxt): number => acc + nxt, 0);
