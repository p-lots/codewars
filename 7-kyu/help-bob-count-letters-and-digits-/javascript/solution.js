const countLettersAndDigits = input => input.split("").filter(ch => /[a-z0-9]/i.test(ch)).length;
