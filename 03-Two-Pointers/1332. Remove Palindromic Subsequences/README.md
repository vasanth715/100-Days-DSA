left = first character
right = last character

while left < right:

    if characters are different:
        return 2

    move both pointers

If the loop finishes:
    return 1





    # 1332. Remove Palindromic Subsequences

## 🧠 Pattern
Two Pointers / Palindrome

## 📌 Problem

Given a string `s` containing only the characters `'a'` and `'b'`.

In one step, we can remove one palindromic subsequence from the string.

Return the minimum number of steps required to make the string empty.

## 💡 Key Observation

Because the string contains only `a` and `b`:

- All `a` characters together form a palindrome.
- All `b` characters together form a palindrome.

Therefore, the answer can only be `1` or `2`.

### Case 1 — String is already a palindrome

If the entire string is a palindrome, we can remove it in one step.

```text
"ababa"