# 정렬 활용
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # 배열-정렬- 문자열로 변환
        s1 = "".join(sorted(s))
        t1 = "".join(sorted(t))

        return s1 == t1
        