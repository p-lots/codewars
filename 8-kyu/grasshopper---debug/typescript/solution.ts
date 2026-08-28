export function weatherInfo(temp: number): string {
  const c = convertToCelsius(temp);
  if (c < 0)
    return (Math.round(c*1e5)/1e5 + " is freezing temperature");
  else
    return (Math.round(c*1e5)/1e5 + " is above freezing temperature");
}

export function convertToCelsius(temperature: number): number {
  const celsius = Math.round(((temperature - 32) * (5/9))*1e5)/1e5;
  return celsius;
}