export function openOrSenior(data: number[][]): string[] {
  return data.map((elem) => elem[0] >= 55 && elem[1] > 7 ? "Senior" : "Open");
}