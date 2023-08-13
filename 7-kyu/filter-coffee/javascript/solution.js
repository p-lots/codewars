const search = (budget, prices) => prices.sort((a, b) => a - b).filter(price => price <= budget).join(",");
