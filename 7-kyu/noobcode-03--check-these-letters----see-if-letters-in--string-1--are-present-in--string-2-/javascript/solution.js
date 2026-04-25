const letterCheck = ([str1, str2]) => [...(str2.toLowerCase())].every(ch => str1.toLowerCase().includes(ch));
