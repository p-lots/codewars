const generateMenu = menuItems => {
  if (menuItems.length === 0) {
    return "";
  }
  return menuItems.map(item => `<a href="${item.url}">${item.text}</a>`).join("");
}