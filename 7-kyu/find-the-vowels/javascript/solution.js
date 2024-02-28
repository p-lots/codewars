const vowelIndices = (word) => word.split("").map((elem, idx) => 'aeiouy'.includes(elem.toLowerCase()) ? idx + 1 : "").filter((elem) => elem !== "");
