const time = (distance, boatSpeed, stream) => {
  const streamSpeed = Number(stream.split(" ")[1]);
  if (stream[0] === "D") {
    boatSpeed += streamSpeed;
  } else {
    boatSpeed -= streamSpeed;
  }
  const t = distance / boatSpeed;
  return Number(t.toFixed(2));
};
