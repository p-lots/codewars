export function time(distance: number, boatSpeed: number, stream: string): number{
  const [streamDir, streamSpeedRaw] = stream.split(" ");
  const streamSpeed = Number(streamSpeedRaw);
  const adjBoatSpeed = (boatSpeed += (streamDir[0] === "U" ? -streamSpeed : streamSpeed));
  return Number((distance / adjBoatSpeed).toFixed(2));
}