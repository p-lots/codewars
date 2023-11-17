const none = (arr, fun) => arr.length === 0 ? true : !arr.every(fun) && !arr.some(fun);
