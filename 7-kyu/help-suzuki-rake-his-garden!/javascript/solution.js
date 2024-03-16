const rakeGarden = (garden) => garden.split(" ").map((elem) => elem === "rock" ? "rock" : "gravel").join(" ");
