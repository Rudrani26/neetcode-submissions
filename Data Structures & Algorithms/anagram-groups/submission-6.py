class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #create a default dic to store
        map_strings = defaultdict(list)

        #iterate through the strings and sort each string in alphabetical order
        #all same order and char strings and under 1 key

        for s in strs:
            key = "".join(sorted(s))
            map_strings[key].append(s)

        return list(map_strings.values())



        