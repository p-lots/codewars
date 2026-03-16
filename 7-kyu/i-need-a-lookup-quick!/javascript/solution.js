Object.defineProperty(
    Array.prototype,
    'toDictionary',
    {value:
        function toDictionary(keyFn, valueFn) {
            return Object.fromEntries(this.map(elem => [keyFn(elem), valueFn ? valueFn(elem) : elem]));
        }
    }
);