const match = (job, candidates) => {
  return candidates.filter((candidate) => {
    const matchesEquity = candidate.desiresEquity ? job.equityMax > 0 : true;
    const matchesLocation = job.locations.includes(candidate.currentLocation) || candidate.desiredLocations.filter((loc) => job.locations.includes(loc)).length > 0;
    return matchesEquity && matchesLocation;
  })
};
