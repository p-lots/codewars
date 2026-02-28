const getVillainName = birthday => {
  const m = ["Evil","Vile","Cruel","Trashy","Despicable","Embarrassing","Disreputable","Atrocious","Twirling","Orange","Terrifying","Awkward"];
  const d = ["Mustache","Pickle","Hood Ornament","Raisin","Recycling Bin","Potato","Tomato","House Cat","Teaspoon","Laundry Basket"];
  
  const firstNameIdx = birthday.getMonth();
  const lastNameIdx = birthday.getDate() % 10;
  return `The ${m[firstNameIdx]} ${d[lastNameIdx]}`;
};
