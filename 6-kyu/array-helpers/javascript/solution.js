Array.prototype.square = function() { return this.map(elem => elem * elem); };

Array.prototype.cube = function() { return this.map(elem => elem * elem * elem); };

Array.prototype.sum = function() { return this.reduce((acc, nxt) => acc + nxt, 0); };

Array.prototype.average = function() { return this.sum() / this.length; };

Array.prototype.even = function() { return this.filter(elem => elem % 2 === 0); };

Array.prototype.odd = function() { return this.filter(elem => elem % 2 === 1); };
