const sumEvenNumbers = input => input.reduce((acc, nxt) => acc + (nxt % 2 === 0 ? nxt : 0), 0); 
