## Task 1 Assumptions and Alternatives

### Assumption

For the final implementation of Task 1, it is assumed that each element in `orders` is a dictionary with at least the keys `status` and `amount` as a number. This aligns with typical order data models and allows the implementation to remain focused and readable without redundant type checks.

### Alternative Implementation

A more defensive version of the function was considered, which includes explicit checks for dictionary types and malformed entries. This version was not selected as the primary solution to avoid unnecessary complexity given the stated assumption, but it is documented as an alternative approach if input data cannot be trusted.

```
def calculate_average_order_value(orders):
    if not orders:
        return 0.0

    total = 0.0
    valid_count = 0

    for order in orders:
        if not isinstance(order, dict):
            continue

        if order.get("status") == "cancelled":
            continue

        amount = order.get("amount")
        try:
            amount = float(amount)
        except (TypeError, ValueError):
            continue

        total += amount
        valid_count += 1

    if valid_count == 0:
        return 0.0

    return total / valid_count
```
