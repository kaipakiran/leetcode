class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return 0
        candidates = {}
        substr = []
        for char in s:
            if char not in substr:
                substr.append(char)
            else:
                str_len = len(substr)
                candidates[str_len] = list(substr)
                substr = substr[substr.index(char)+1:]
                substr.append(char)
        str_len = len(substr)
        candidates[str_len] = list(substr)
        return max(candidates.keys()) if len(candidates.keys()) > 0 else len(substr)