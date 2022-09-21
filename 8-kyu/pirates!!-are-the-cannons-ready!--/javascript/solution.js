const cannonsReady = (gunners) => Object.entries(gunners).every(elem => elem[1] === 'aye') ? "Fire!" : "Shiver me timbers!";
