const sumOfIntegersInString = s => s.split(/\D/g).filter((elem) => elem).reduce((acc, nxt) => acc + parseInt(nxt), 0);
