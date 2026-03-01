const killcount = (counselors, jason) => counselors.filter(([ name, intel ]) => intel < jason).map(([ name, intel ]) => name);
