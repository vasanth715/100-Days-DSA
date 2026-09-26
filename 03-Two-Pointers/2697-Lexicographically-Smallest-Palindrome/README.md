## ⚙️ Algorithm

1. Initialize `left` at the beginning of the array/string.
2. Initialize `right` at the last index.
3. While `left < right`:
   - Compare the elements/characters at `left` and `right`.
   - If they satisfy the required condition, perform the required operation.
   - Move `left` forward.
   - Move `right` backward.
4. Continue until the pointers meet.
5. Return the result.




## ⚙️ Algorithm

```text
left = 0
right = last index

while left < right:

    if characters are different:
        keep the smaller character on both sides

    move left forward
    move right backward

return the resulting string





This is actually **very useful for your 100 Days DSA revision**, because when you open the README after 2–3 months, you don't need to read the whole explanation. You can quickly see:

**Problem → Pattern → Algorithm → Code → Complexity → What I Learned**

🔥 So our standard README structure from now on will be:

```text
# Problem

🧠 Pattern

📌 Problem

💡 Approach

⚙️ Algorithm        ← ALWAYS INCLUDE THIS

🔍 Dry Run

💻 Solution

⏱ Complexity

🎯 What I Learned