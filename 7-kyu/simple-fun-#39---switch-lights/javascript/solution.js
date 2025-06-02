function switchLights(candles) {
  let lights = [...candles];
  for (let i = 0; i < lights.length; i++) {
    if (lights[i] === 1) {
      for (let j = i; j >= 0; j--) {
        lights[j] = lights[j] === 1 ? 0 : 1;
      }
    }
  }
  return lights;
}