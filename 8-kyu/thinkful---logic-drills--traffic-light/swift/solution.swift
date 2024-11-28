export const updateLight = (current: string): string => {
  const lights = ["green", "yellow", "red"];
  const currLight = lights.indexOf(current);
  const nextLight = (currLight + 1) % lights.length;
  return lights[nextLight];
};
