const whoTookTheCarKey = message => message.map(letter => String.fromCharCode(parseInt(letter, 2))).join("");
