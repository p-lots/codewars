export const generateShape = (int: number): string => {
  return Array.from({ length: int }, (_) => "+".repeat(int)).join("\n");
};
