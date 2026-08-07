class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) -1
        while left < right:
            while s[left].isalpha() != True and left < right:
                left +=1
            while s[right].isalpha() != True and left < right:
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True