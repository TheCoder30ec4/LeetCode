class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = 0
        if len(needle) == 0:
            return 0

        while index+len(needle) <= len(haystack):

            if needle == haystack[index:index+len(needle)]:
                return index 
            index = index+1

        return -1

