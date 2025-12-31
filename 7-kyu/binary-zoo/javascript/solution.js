const countTheAnimals = animals => Object.values(animals).map(count => Number.parseInt(count, 2)).reduce((acc, nxt) => acc + nxt, 0);
