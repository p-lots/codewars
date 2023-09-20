const { Buffer } = require('node:buffer');

String.prototype.toBase64 = function() {
  const buf = Buffer.from(this);
  return buf.toString('base64');
}

String.prototype.fromBase64 = function() {
  const buf = Buffer.from(this, 'base64');
  return buf.toString();
}
