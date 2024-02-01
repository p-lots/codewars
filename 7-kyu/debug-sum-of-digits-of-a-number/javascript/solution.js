const getSumOfDigits = (integer) => integer.toString().split("").reduce((acc, nxt) => acc + parseInt(nxt), 0);
