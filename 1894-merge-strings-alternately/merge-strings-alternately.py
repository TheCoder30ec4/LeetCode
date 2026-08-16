class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        final_str = ""

        i = len(word1)
        j = len(word2)

        while i>0 or j>0:

            if i!=0:
                final_str += word1[abs(i-len(word1))]
                i -=1
            if j!=0:
                final_str += word2[abs(j-len(word2))]
                j -=1

        return final_str
        