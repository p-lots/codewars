const areEquallyStrong = (yourLeft, yourRight, friendsLeft, friendsRight) => {
  const ret = (yourLeft === friendsLeft && yourRight === friendsRight) || (yourLeft === friendsRight && yourRight === friendsLeft);
  return ret;
};
