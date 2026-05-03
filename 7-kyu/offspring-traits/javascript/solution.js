const bearFur = bears => {
  const validBears = ['black', 'brown', 'white'];
  if (!bears.every(bear => validBears.includes(bear))) {
    return "unknown";
  }
  const [firstBear, secondBear] = bears;
  if (firstBear === secondBear) {
    return firstBear;
  }
  const lookup = {
    white: {
      black: "grey",
      brown: "light brown"
    },
    brown: {
      white: "light brown",
      black: "dark brown"
    },
    black: {
      white: "grey",
      brown: "dark brown"
    }
  };
  return lookup[firstBear][secondBear] || "unknown";
};