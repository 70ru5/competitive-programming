class Solution:
    def mergeAlternately(self, word1, word2):
        
        s = ""
        len1 = len(word1)
        len2 = len(word2)
        

        def merge(self, word1, word2):
            s = ""
            for i in range(min(len1, len2)):
                s += word1[i] + word2[i]
                i += 1
            return s

        if len1 == len2:
            s =merge(self, word1, word2)
        elif len1 > len2:
            s = merge(self, word1, word2)
            s += word1[len2:]
        else:
            s = merge(self, word1, word2)
            s += word2[len1:]

        return s