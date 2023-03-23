const zombie_shootout = (zombies, range, ammo) => {
  if (zombies === 0) {
    return "You shot all 0 zombies.";
  }
  let zombs = zombies;
  while (range > 0 && ammo > 0) {
    zombs--;
    if (zombs === 0) {
      return `You shot all ${zombies} zombies.`; 
    }
    range -= 0.5;
    ammo--;
  }
  if (ammo === 0 && range > 0) {
    return `You shot ${zombies - zombs} zombies before being eaten: ran out of ammo.`;
  }
  return `You shot ${zombies - zombs} zombies before being eaten: overwhelmed.`;
}