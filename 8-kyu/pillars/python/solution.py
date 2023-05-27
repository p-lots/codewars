const pillars = (num_pill, dist, width) => num_pill < 2 ? 0 : dist * 100 * (num_pill - 1) + width * (num_pill - 2);
