const automorphic = n => (n ** 2).toString().slice(-(n.toString().length)) === n.toString() ? "Automorphic" : "Not!!";
