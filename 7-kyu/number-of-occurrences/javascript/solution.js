Object.defineProperty(Array.prototype, 'numberOfOccurrences', { 
  value : function numberOfOccurrences(val) {
    return this.filter(elem => elem === val).length;
  }
});