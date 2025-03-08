export function findNextSquare(sq: number): number {
  const root = Math.round(sq ** 0.5);
  return root * root === sq ? (root + 1) ** 2 : -1;
}