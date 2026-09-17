class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            # print(key)
            groups[key].append(s)
        # print(groups.values())
        
        return list(groups.values())