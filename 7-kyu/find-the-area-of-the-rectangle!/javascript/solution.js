const area = (diagonal, length) => diagonal > length ? Math.round(Math.sqrt(diagonal ** 2 - length ** 2) * length * 100) / 100 : "Not a rectangle";
