export const strCount = (str: string, letter: string): number => str.split("").filter(ch => ch === letter).length;