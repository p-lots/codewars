const f = (x, cc) => {
  switch (x) {
      case cc.a:
      return cc.b;
      case cc.b:
      return cc.c;
      case cc.c:
      return cc.a;
      default:
      return;
  };
};
