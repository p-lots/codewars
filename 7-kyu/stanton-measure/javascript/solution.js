/*
  function:- stantonMeasure
  input:- integer array
  output:- stanton measure of the array
*/
const stantonMeasure = array => {
  const oneCount = array.filter(elem => elem === 1).length;
  return array.filter(elem => elem === oneCount).length;
}
