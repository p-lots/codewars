// return an index of section or -1 if past last section
// scrollY is a positive integer and sizes is an array of positive integers
const getSectionIdFromScroll = (scrollY, sizes) => {
  let scrolledPixels = 0;
  let sectionId = -1;
  for (let i = 0; i < sizes.length; i++) {
    scrolledPixels += sizes[i];
    if (scrolledPixels > scrollY) {
      sectionId = i;
      break;
    }
  }
  return sectionId;
}