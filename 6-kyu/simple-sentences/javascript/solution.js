function makeSentence(parts) {
  return parts.join(" ").replace(/ ,/g, ",").replace(/\./g, "").trim() + ".";  
}