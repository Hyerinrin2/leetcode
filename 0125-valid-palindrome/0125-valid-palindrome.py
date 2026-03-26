class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_c = ""
        for c in s.lower():
            if c.isalnum(): # 특수문자 판별
               new_c += c
        return new_c == new_c[::-1]
        