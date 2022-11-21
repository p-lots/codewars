const toNumberArray = stringarray => stringarray.map(elem => typeof elem === "string" ? parseFloat(elem) : elem);
