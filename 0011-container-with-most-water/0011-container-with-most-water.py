class Solution:
    def maxArea(self, height: List[int]) -> int:

        # 정렬 후 포인터로 곱했을 때 최대인 두 수를 찾기
        left=0
        right = len(height) -1 
        max_a= 0
        

        while left < right:
            area = min(height[left],height[right]) * (right-left)

            max_a = max(max_a, area)

            if height[left] < height[right]:
                left +=1
            else:
                right-=1

        return max_a
        