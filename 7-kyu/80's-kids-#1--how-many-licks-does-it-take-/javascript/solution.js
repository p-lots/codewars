const totalLicks = env => {
  const avgLicksBase = 252;
  const totalEnvLicks = Object.values(env).reduce((acc, nxt) => acc + nxt, 0) || 0;
  let additionalChallenge = "";
  if (Object.values(env).some(licks => licks > 0)) {
    let challengeType = Object.keys(env)[0];
    let mostLicks = Object.values(env)[0];
    for (const [challenge, licks] of Object.entries(env)) {
      if (licks > mostLicks) {
        challengeType = challenge;
        mostLicks = licks;
      }
    }
    additionalChallenge = ` The toughest challenge was ${challengeType}.`;
  }
  return `It took ${avgLicksBase + totalEnvLicks} licks to get to the tootsie roll center of a tootsie pop.` + additionalChallenge;
};
