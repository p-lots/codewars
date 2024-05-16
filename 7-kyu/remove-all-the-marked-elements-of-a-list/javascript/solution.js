Array.prototype.remove_ = function(integer_list, values_list) {
  return integer_list.filter(elem => !values_list.includes(elem));
};
