const DNAStrand = dna => {
  const lookup = {G: "C", C: "G", T: "A", A: "T"};
  return dna.split("").map((elem) => lookup[elem]).join("");
};