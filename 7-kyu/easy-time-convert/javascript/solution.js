const timeConvert = (num) => {
  const hours = Math.max(Math.floor(num / 60), 0).toString().padStart(2, '0');
  const minutes = Math.max(num % 60, 0).toString().padStart(2, '0');
  return `${hours}:${minutes}`;
}