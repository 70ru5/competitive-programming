class Solution:
    def mergeAlternately(self, word1, word2):
        result = ""
        len1, len2 = len(word1), len(word2)
        i = 0
        
        while i < len1 or i < len2:
            if i < len1:
                result += word1[i]
            if i < len2:
                result += word2[i]
            i += 1
        
        return result