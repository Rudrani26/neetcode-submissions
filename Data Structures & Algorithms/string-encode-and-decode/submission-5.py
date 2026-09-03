class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = []
        #code would be length of the string,#,string like 5#hello
        for s in strs:
            encodedString.append(str(len(s)))
            encodedString.append('#')
            encodedString.append(s)
        return "".join(encodedString) #join all together

    def decode(self, s: str) -> List[str]:
        #have 2 pointers i and j, i will scan each char and j will look for #, after hash the word is there and we will crop out out chars from j till length of the word as in the code and then join

        decodString = []
        i = 0

        while i < len(s):
            j = i
            
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            i = j + 1
            j = i + length

            decodString.append(s[i:j])

            i = j
        
        return decodString


