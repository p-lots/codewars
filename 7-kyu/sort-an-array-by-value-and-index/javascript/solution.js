const sortByValueAndIndex = (array) => array.map((elem, idx) => [elem, elem * (idx + 1)]).sort((a, b) => a[1] - b[1]).map((elem) => elem[0]);
