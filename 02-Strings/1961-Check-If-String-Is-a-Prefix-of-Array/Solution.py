class Solution(object):
    def isPrefixString(self, s, words):
        temp = ""

        for word in words:
            temp += word

            if temp == s:
                return True

            if len(temp) > len(s):
                return False

        return False