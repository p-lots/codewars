const dropzone = ([fireX, fireY], dropzones) => {
  const distances = dropzones.map(([dropX, dropY]) => Math.sqrt((dropX - fireX) ** 2 + (dropY - fireY) ** 2));
  const minIdx = distances.findIndex(dist => dist === Math.min(...distances));
  return dropzones[minIdx];
};
