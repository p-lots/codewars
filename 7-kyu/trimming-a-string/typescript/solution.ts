export function trim(str: string, size: number): string {
  if (str.length <= size) {
    return str;
  } else if (str.length <= 3 || size <= 3) {
    return `${str.slice(0, size)}...`;
  }
  return `${str.slice(0, size - 3)}...`;
}