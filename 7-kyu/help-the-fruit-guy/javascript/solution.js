const removeRotten = bagOfFruits => bagOfFruits ? bagOfFruits.map((elem) => elem.replace("rotten", "").toLowerCase()) : [];
