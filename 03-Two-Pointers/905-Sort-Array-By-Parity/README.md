# 905. Sort Array By Parity

## 🧠 Pattern
Two Pointers

## 📌 Problem

Given an integer array `nums`, move all even integers to the beginning
of the array followed by all odd integers.

## 💡 Approach

Use two pointers:

- `l` starts from the beginning.
- `r` starts from the end.
- If `nums[l]` is even, it is already in the correct position.
- If `nums[r]` is odd, it is already in the correct position.
- Otherwise, `nums[l]` is odd and `nums[r]` is even, so swap them.
- Move the pointers accordingly.

## 🔄 Example

Input:

[3,1,2,4]

Output:

[4,2,1,3]

Any arrangement with all even numbers before all odd numbers is valid.

## 💻 Solution

See `Solution.py`

## ⏱ Complexity

Time: O(n)

Space: O(1)

## 🎯 What I Learned

- Two Pointer technique
- Checking the value using `% 2`
- In-place swapping
- Moving pointers based on conditions




## 🧠 Pseudocode first

left = 0
right = last index

while left < right:

    if left value is even:
        move left

    else if right value is odd:
        move right

    else:
        swap left value and right value
        move both pointers

return nums