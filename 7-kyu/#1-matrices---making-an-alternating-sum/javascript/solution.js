const scoreMatrix = matrix => matrix.reduce((rowAcc, row, rowIdx) => rowAcc + row.reduce((acc, num, idx) => acc + ((-1) ** (rowIdx + idx) * num), 0), 0);
