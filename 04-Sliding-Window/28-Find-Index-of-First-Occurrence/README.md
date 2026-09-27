# 28. Find the Index of the First Occurrence in a String

## 🧠 Pattern

Fixed-Size Sliding Window

## 📌 Problem

Given two strings `haystack` and `needle`, find the index of the
first occurrence of `needle` inside `haystack`.

Return `-1` if `needle` does not occur.

---

## 🔍 Pattern Recognition

### Keywords

- Find a substring
- First occurrence
- Pattern inside another string
- Consecutive characters
- Fixed-length pattern
- String matching

### Think:

```text
Needle = pattern
        ↓
Pattern has fixed length
        ↓
Check same-sized parts of haystack
        ↓
Fixed-Size Sliding Window




### Algorithm

window_size = length of needle

left = 0
right = window_size
index = 0

while the window is inside haystack:

    take substring haystack[left:right]

    if substring == needle:
        return index

    move the window one position:
        left += 1
        right += 1
        index += 1

return -1