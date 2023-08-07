const add = (...args) => Math.round(args.reduce((accum, next, idx) => accum + (next / (idx + 1)), 0));
