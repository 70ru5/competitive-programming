import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        length = math.gcd(len(str1), len(str2))
        candidate = str1[:length]

        checker = 0
        
        string = candidate
        while len(string) <= len(str1):
            if string == str1:
                break
            elif string != str1[:len(string)]:
                checker += 1
                break
            else:
                string += candidate

        string = candidate
        while len(string) <= len(str2):
            if string == str2:
                break
            elif string != str2[:len(string)]:
                checker += 1
                break
            else:
                string += candidate

        if checker == 0:
            return candidate
        else:
            return 
