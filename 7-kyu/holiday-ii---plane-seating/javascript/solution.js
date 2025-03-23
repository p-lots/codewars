const planeSeat = (a) => {
  if (/[IJ]/.test(a) || a.length === 3 && parseInt(a.slice(0, 2)) > 60) {
    return "No Seat!!";
  }
  const section = a.length === 3 ? parseInt(a.slice(0, 2)) : parseInt(a.slice(0, 1));
  const cluster = a.at(-1);
  let sectionLocation = "";
  let clusterLocation = "";
  if (section < 21) {
    sectionLocation = "Front";
  } else if (section < 41) {
    sectionLocation = "Middle";
  } else {
    sectionLocation = "Back";
  }
  if (cluster >= "A" && cluster <= "C") {
    clusterLocation = "Left";
  } else if (cluster >= "D" && cluster <= "F") {
    clusterLocation = "Middle";
  } else {
    clusterLocation = "Right";
  }
  return `${sectionLocation}-${clusterLocation}`;
};
