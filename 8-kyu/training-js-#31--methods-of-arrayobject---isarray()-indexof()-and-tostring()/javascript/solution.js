const blackAndWhite = (arr) => Array.isArray(arr) ? `It's a ${arr.indexOf(5) !== -1 && arr.indexOf(13) !== -1 ? "black" : "white"} array` : "It's a fake array";
