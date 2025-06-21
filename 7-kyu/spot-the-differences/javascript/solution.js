const spot = (s1, s2) => s1.split("")
    .map((elem, idx) => elem !== s2[idx] ? idx : null)
    .filter(elem => elem !== null);
