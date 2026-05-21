const quicksum = packet => {
  if (/[^A-Z ]/.test(packet)) {
    return 0;
  }
  return packet.split("").reduce((acc, nxt, idx) => {
    return acc + (/[A-Z]/.test(nxt) ? (nxt.charCodeAt() - 64) * (idx + 1) : 0);
  }, 0);
};
