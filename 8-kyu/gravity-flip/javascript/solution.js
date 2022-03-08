const flip = (d, a) => d === 'R' ? a.sort((lhs, rhs) => lhs - rhs) : a.sort((lhs, rhs) => lhs - rhs).reverse();
