class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hashmap = {}

        return ''.join(sorted(s)) == ''.join(sorted(t))