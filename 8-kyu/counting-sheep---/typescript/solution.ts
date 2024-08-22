export const countSheeps = (arrayOfSheep: (boolean | undefined | null)[]): number => arrayOfSheep.filter(Boolean).length;
