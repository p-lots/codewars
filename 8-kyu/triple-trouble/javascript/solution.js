export const tripleTrouble = (one: string, two: string, three: string): string => Array.from({ length: one.length }, (_, idx) => one[idx] + two[idx] + three[idx]).join("");
