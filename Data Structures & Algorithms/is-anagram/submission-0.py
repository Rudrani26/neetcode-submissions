class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #check whether the length of both the strings is same if not, its an immediate false
        if len(s)!=len(t):
            return False
        
        #we keep a count of the characters
        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val !=0:
                return False
        return True
                
        