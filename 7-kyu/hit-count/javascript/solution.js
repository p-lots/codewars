const counterEffect = hitCount => [...hitCount].map(n => Array.from( { length: +n + 1 }, (_, idx) => idx));
