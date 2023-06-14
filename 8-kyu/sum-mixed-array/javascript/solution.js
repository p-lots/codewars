const sumMix = x => x.map((elem) => typeof elem === 'string' ? parseInt(elem) : elem).reduce((acc, nxt) => acc + nxt, 0);
