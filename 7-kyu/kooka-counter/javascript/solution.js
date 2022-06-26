const kookaCounter = laughing => laughing.split("").reduce((accum, currCh, i, arr) => ((i % 2 === 0 && currCh !== arr[i + 2]) ? accum + 1 : accum), 0);
