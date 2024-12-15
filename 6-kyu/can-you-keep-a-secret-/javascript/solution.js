function createSecretHolder(secret) {
  class secretHolder {
    constructor() {
      this.$secret = secret;
    }
    setSecret(_secret) {
      this.$secret = _secret;
    }
    getSecret() {
      return this.$secret;
    }
  }
  var _secretHolder = new secretHolder(secret);
  return _secretHolder;
}