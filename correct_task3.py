# Write your corrected implementation for Task 3 here.
# Do not modify `task3.py`.

def average_valid_measurements(values):
    if not values:
        return 0.0

    total = 0.0
    valid_count = 0

    for value in values:
        if value is None:
            continue
        
        number = float(value)

        total += number
        valid_count += 1

    if valid_count == 0:
        return 0.0

    return total / valid_count
