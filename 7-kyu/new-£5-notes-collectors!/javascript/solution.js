const getNewNotes = (salary, bills) => Math.max(0, Math.floor((salary - bills.reduce((acc, nxt) => acc + nxt, 0)) / 5))
