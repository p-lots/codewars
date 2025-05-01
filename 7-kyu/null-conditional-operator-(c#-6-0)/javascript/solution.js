Car.prototype.getNumberOfGears = function() {
  return this?.engine?.gearBox?.numberOfGears ?? null;
}