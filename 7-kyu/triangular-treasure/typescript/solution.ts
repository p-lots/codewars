// Return the nth triangular number
export const triangular = (n: number): number => n > 0 ? Math.floor(n * (n + 1) / 2) : 0;
