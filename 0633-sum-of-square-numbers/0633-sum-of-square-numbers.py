class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        left = 0
        right = int(sqrt(c))

        while left <= right:
            if left**2 + right**2 == c:
                return True
            elif  left*left + right*right < c:
                left+=1
            else:
                right-=1
        return False            
        