# 942. DI String Match

## 🧠 Pattern
Two Pointers / Greedy

## 📌 Problem

Given a string `s` containing only `I` and `D`, construct a permutation
of numbers from `0` to `n` that follows the pattern.

- `I` means Increasing
- `D` means Decreasing

## 💡 Approach

Use two pointers:

- `low = 0`
- `high = n`

For every character:

### If character is `I`

Choose the smallest available number.

```text
result.append(low)
low += 1






low = 0
high = n

for every character:

    if I:
        take low
        increase low

    else:
        take high
        decrease high

after the loop:
    take the remaining number