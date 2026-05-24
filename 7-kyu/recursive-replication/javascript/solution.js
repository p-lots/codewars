const replicate = (times, number) => times > 0 ? [number, ...replicate(times - 1, number)] : [];
