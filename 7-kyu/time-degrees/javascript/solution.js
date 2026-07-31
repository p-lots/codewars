const clockDegree = s => {
  const [hours, minutes] = s.split(":").map(Number);
  if (hours < 0 || hours > 23 || minutes < 0 || minutes > 59 || Number.isNaN(hours) || Number.isNaN(minutes)) {
    return "Check your time !";
  }
  const degreesPerHour = 360 / 12;
  const degreesPerMinute = 360 / 60;
  const hourDegrees = degreesPerHour * (hours === 0 || hours === 12 ? 12 : hours % 12);
  const minuteDegrees = degreesPerMinute * (minutes === 0 ? 60 : minutes);
  return `${hourDegrees}:${minuteDegrees}`;
};
