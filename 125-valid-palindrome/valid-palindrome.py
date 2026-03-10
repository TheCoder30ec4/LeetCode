import re
class Solution:
    def isPalindrome(self, s: str) -> bool:


        def _remove_shit(text:str)->str:

            return re.sub(r'[^a-zA-Z0-9]', '', text).lower()

       
        clean_shit = _remove_shit(s)
        left_pointer = 0
        right_pointer = len(clean_shit)-1
        print(clean_shit)
        while left_pointer < right_pointer:

            if clean_shit[left_pointer] != clean_shit[right_pointer]:
                return False
            
            left_pointer +=1
            right_pointer -=1

        return True





        