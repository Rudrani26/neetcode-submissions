class Solution:

    def encode(self, strs: List[str]) -> str:
        #we use a delimiter # and calculate the length of the string
        #it should look like 5#hello for "hello"
        result = ""
        for s in strs:
            result += str(len(s)) + '#' + s
        return result

    def decode(self, s: str) -> List[str]:
        #create an empty list
        result = []
        i = 0
        while i < len(s): #ensures entire string is parsed
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            result.append(s[j+1:j+1+length])
            i = j+1+length
        return result

