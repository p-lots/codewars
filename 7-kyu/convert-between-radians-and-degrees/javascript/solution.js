Math.degrees = function(rads) {
  return `${Math.round((rads * 180 / Math.PI) * 100) / 100}deg`;
}

Math.radians = function(degs) {
  return `${Math.round((degs * Math.PI / 180) * 100) / 100}rad`;
}