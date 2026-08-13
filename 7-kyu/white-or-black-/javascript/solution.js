const mineColor = (file, rank) => (file.charCodeAt(0) + rank) % 2 ? "white" : "black"
