## Task
You have a messy fridge! To prevent food waste, you need to decide what to eat first based on two factors: **expiry date** and **quantity**.

Write a function that takes a list of food items and returns their names sorted by **urgency score**.

### Data Format
Each food item is an **object** that has the following attributes:

<!-- Add languages that use snake_case to the `if` list below -->
```if:python,
* `name`: The name of the food. (string)
* `expiry_days`: Days until it expires. (integer; can be negative)
* `is_almost_empty`: true if you only have a little bit left. (boolean)
```

<!-- Add languages that use camelCase to the `if` list below -->
```if:javascript,
* `name`: The name of the food. (string)
* `expiryDays`: Days until it expires. (integer; can be negative)
* `isAlmostEmpty`: true if you only have a little bit left. (boolean)
```

### Sorting Rules
1. **Discard Spoiled**: If the days to expiry are less than 0, the item is spoiled. **Do not include it in the output.**
2. **Empty First**: Items that are almost empty come before items that are not.
3. **Expiry**: Within those groups, items with the **lowest** days to expiry come first.
4. **Alphabetical**: If both status and expiry are the same, sort by name **alphabetically**.

### Example
When provided with the following list of food items:
|  Name        | Days to Expiry | Is Almost Empty? |
|--------------|----------------|------------------|
| Milk         | 3              | false            |
| Jam          | 3              | true             |
| Yogurt       | 1              | false            |
| Old Meat     | -1             | true             |
| Today's Tofu | 0              | false            |

You should return:

```["Jam", "Today's Tofu", "Yogurt", "Milk"]```

In that order.