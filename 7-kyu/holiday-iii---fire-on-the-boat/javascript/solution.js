const fireFight = (s) => s.split(" ")
    .map((elem) => elem === "Fire" ? "~~" : elem)
    .join(" ");
