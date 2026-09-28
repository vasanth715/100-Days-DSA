class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):

        words = sentence.split()

        for i in range(len(words)):

            word = words[i]

            if len(word) >= len(searchWord):

                match = True

                for j in range(len(searchWord)):

                    if word[j] != searchWord[j]:
                        match = False
                        break

                if match:
                    return i + 1

        return -1