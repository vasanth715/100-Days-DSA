split sentence into words

for every word:

    if word is shorter than searchWord:
        skip it

    left = 0
    right = 0

    while right < searchWord length:

        if word[left] != searchWord[right]:
            stop

        move left
        move right

    if right reached searchWord length:
        return word index + 1

return -1