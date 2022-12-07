const FilterString = value => parseInt(value.split("").filter(elem => elem >= "0" && elem <= "9").join(""));
