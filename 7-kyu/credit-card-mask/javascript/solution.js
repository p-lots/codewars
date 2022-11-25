const maskify = cc => cc.length <= 4 ? cc : cc.split("").map((ch, i) => i < cc.length - 4 ? "#" : ch).join("");
