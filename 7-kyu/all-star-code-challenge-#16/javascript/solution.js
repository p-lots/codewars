const noRepeat = str => str.split("").find(ch => str.indexOf(ch) === str.lastIndexOf(ch));
