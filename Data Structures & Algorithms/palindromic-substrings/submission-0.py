class Solution:
    def countSubstrings(self, s: str) -> int:
        startIdx = 0
        resLen = 0
        count = 0

        #loop the string
        for i in range(len(s)):
            #ODD LENGTH
            #set both pointers to the current character
            l, r = i, i
            #while they are same and in bounds of the strong
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if  resLen < (r-l+1):
                    startIdx = l
                    resLen = r - l + 1
                    
                l -= 1
                r += 1
                count += 1
            
            #EVEN LENGTH
            #set both pointers to current character and the next
            l, r = i, i + 1
            #while they are same and in bounds of the strong
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if  resLen < (r-l+1):
                    startIdx = l
                    resLen = r - l + 1
                    
                l -= 1
                r += 1
                count += 1
            
        return count


    #we check go through the string once and check for each letter if its
    #right and left character are same 
    #if yes we keep the start index of that substring as the left pointer and
    #and set the length as r-l+1 and then check left and right of that substring
        