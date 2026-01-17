# AI Code Review Assignment (Python)

## Candidate

- Name: Kiya Kebe
- Approximate time spent: 75 Min

---

# Task 1 — Average Order Value

## 1) Code Review Findings

### Critical bugs

- Division by the total number of orders instead of the number of non-cancelled orders produces incorrect averages.

- Possible ZeroDivisionError when the input list is empty.

### Edge cases & risks

- All orders being cancelled results in division by zero.

- Orders with non-numeric or missing amount values can cause runtime errors.

- The function assumes all orders have a consistent structure without validation.

### Code quality / design issues

- The variable count is misleading, as it does not represent the number of averaged orders.

- Business logic and assumptions about input data are implicit rather than explicit.

- Lack of defensive handling for malformed numeric values.

## 2) Proposed Fixes / Improvements

### Summary of changes

- Track only non-cancelled orders when computing the average.

- Guard against empty input and cases where no valid orders exist.

- Convert order amounts to floats safely to avoid runtime errors.

- Make the averaging logic explicit and mathematically correct.

### Corrected code

See `correct_task1.py`

### Testing Considerations

- Empty order list to ensure safe default behavior.

- All orders cancelled to verify no division error occurs.

- Mixed cancelled and active orders.

- Orders with missing or non-numeric amount values.

- Large monetary values to confirm numeric stability.

## 3) Explanation Review & Rewrite

### AI-generated explanation (original)

> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average.

### Issues in original explanation

- Incorrectly states that cancelled orders are excluded from the divisor.

- Does not mention error cases such as empty input or invalid amounts.

- Overstates correctness of the implementation.

### Rewritten explanation

- This function calculates the average order value by summing the amounts of non-cancelled orders and dividing by the number of valid, non-cancelled entries. It safely handles empty input and ignores orders with invalid amount values.

## 4) Final Judgment

- Decision: Request Changes

- Justification: The original implementation contains a fundamental mathematical error and lacks basic safeguards against invalid input.

- Confidence & unknowns: High confidence in the identified issues and fixes; assumes order objects follow a consistent dictionary structure.

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings

### Critical bugs

- The original implementation classifies any string containing `@` as a valid email, which is fundamentally incorrect.
- It does not verify the presence of a domain, top-level domain, or proper structure.

### Edge cases & risks

- Non-string inputs can raise runtime errors.
- Whitespace around email strings is not handled.
- Invalid formats such as `"@"`, `"user@"`, or `"@domain.com"` are incorrectly counted as valid.
- Overly permissive validation may allow malformed addresses.

### Code quality / design issues

- Function behavior does not match its name or documented intent.
- Validation logic is oversimplified and misleading.
- Email verification is not centralized or reusable.

---

## 2) Proposed Fixes / Improvements

### Summary of changes

- Introduced a compiled regular expression to validate basic email structure.
- Stripped whitespace from inputs before validation.
- Safely ignored non-string entries.
- Ensured behavior matches the documented purpose of counting valid email addresses.

### Corrected code

See `correct_task2.py`

### Testing Considerations

- Empty input list to confirm safe default behavior.
- Mixed valid and invalid email formats.
- Inputs containing leading or trailing whitespace.
- Non-string entries such as `None` or integers.
- Boundary cases like minimal valid emails and long domain names.

---

## 3) Explanation Review & Rewrite

### AI-generated explanation (original)

> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation

- Overstates correctness of validation.
- Does not describe how validity is determined.
- Implies safety guarantees that were not present in the original implementation.

### Rewritten explanation

- This function counts email addresses that match a basic structural validation rule using a regular expression. It trims whitespace, ignores non-string inputs, and safely handles empty lists without raising errors.

---

## 4) Final Judgment

- Decision: **Request Changes**
- Justification: The original implementation fails to perform meaningful email validation and does not meet its stated intent.
- Confidence & unknowns: High confidence in the fixes; full RFC-compliant email validation is intentionally out of scope.

---

## Task 3 — Aggregate Valid Measurements

---

## 1) Code Review Findings

### Critical bugs

- The original implementation divides by the total number of input values instead of the number of valid measurements, producing incorrect averages.
- A `ZeroDivisionError` can occur when all values are `None`.

### Edge cases & risks

- Empty input lists are not handled safely.
- Non-numeric values can cause runtime failures in the original code.
- Boolean values may be unintentionally treated as numeric measurements.

### Code quality / design issues

- The variable `count` in the original code does not represent the number of averaged values.
- Input assumptions are implicit and undocumented.
- Error handling logic obscures the intended data contract.

---

## 2) Proposed Fixes / Improvements

### Summary of changes

- Average only valid, non-`None` measurements.
- Explicitly track the count of valid values.
- Guard against empty input and empty valid sets.
- Simplify numeric conversion based on a stricter input contract.

### Corrected code

See `correct_task3.py`

### Testing Considerations

- Empty list input.
- Lists containing only `None`.
- Mixed numeric types (int, float).
- Large numeric values.
- Lists guaranteed to contain only numeric or `None` values, per assumption.

---

## 3) Explanation Review & Rewrite

### AI-generated explanation (original)

> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average.

### Issues in original explanation

- Claims safe handling of mixed input types, which is not true.
- Does not mention division-by-zero risk.
- Overstates correctness of the averaging logic.

### Rewritten explanation

- This function computes the average of numeric measurements by ignoring `None` values and averaging the remaining entries. It assumes all non-`None` values are valid numeric inputs and safely handles empty input by returning zero.

---

## 4) Final Judgment

- Decision: **Request Changes**
- Justification: The original implementation contains a mathematical error and unsafe assumptions that can lead to runtime failures.
- Confidence & unknowns: High confidence in the corrected logic; correctness depends on the stated numeric input assumption.

---
