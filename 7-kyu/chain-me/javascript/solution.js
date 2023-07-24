const chain = (input, fs) => fs.reduce((acc, nxt) => nxt(acc), input);
