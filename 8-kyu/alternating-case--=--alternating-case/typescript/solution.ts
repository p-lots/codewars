export const toAlternatingCase = (s: string): string => s.split("")
    .map(ch => ch.toUpperCase() === ch ? ch.toLowerCase() : ch.toUpperCase())
    .join("");
