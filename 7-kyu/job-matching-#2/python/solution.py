def matches_criteria(job, candidate):
    equity_match = job['equity_max'] > 0 if candidate['desires_equity'] else True
    location_match = candidate['current_location'] in job['locations'] or any(loc in job['locations'] for loc in candidate['desired_locations'])
    return equity_match and location_match

def match(job, candidates):
    return [candidate for candidate in candidates if matches_criteria(job, candidate)]
