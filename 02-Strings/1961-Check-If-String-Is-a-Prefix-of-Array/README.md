# 1961. Check If String Is a Prefix of Array

## 🧠 Pattern

String Traversal + Incremental Construction + Prefix Checking

## 📌 Problem

Given a string `s` and an array of strings `words`, determine whether
`s` can be formed by concatenating the first `k` strings in `words`.

The words must be taken from the beginning without skipping any word.

## 💡 Approach

Use a temporary string `temp` to build the prefix step by step.

- Start with an empty string.
- Traverse `words` from left to right.
- Add each word to `temp`.
- After every addition, check whether `temp` equals `s`.
- If `temp` becomes longer than `s`, return `False`.
- If the loop finishes without finding a match, return `False`.

## ⚙️ Algorithm

```text
temp = ""

for each word in words:

    append word to temp

    if temp == s:
        return True

    if length of temp > length of s:
        return False

return False