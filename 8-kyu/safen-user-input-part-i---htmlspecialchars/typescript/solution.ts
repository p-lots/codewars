const htmlspecialchars = formData => {
  const lookup = {"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;"};
  for (const key in lookup) {
    formData = formData.replace(new RegExp(key, 'g'), lookup[key]);
  }
  return formData;
};
