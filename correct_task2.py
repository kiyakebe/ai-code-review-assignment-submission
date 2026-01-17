# Write your corrected implementation for Task 2 here.
# Do not modify `task2.py`.

import re

EMAIL_REGEX = re.compile(
    r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
)

def count_valid_emails(emails):
    if not emails:
        return 0

    count = 0

    for email in emails:
        if not isinstance(email, str):
            continue

        email = email.strip()

        if EMAIL_REGEX.match(email):
            count += 1

    return count
