class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ## 하나는 for문으로 고정하고 나머지 두 개로 투 포인터
        result = []
        i = 0
        
        # 정렬
        nums.sort()

        for i in range(0,len(nums)-1):
            if i > 0 and nums[i] == nums[i-1]: # i에 대한 중복 처리
                continue
            left = i +1
            right = len(nums) -1

            # 한 번의 i에서도 여러 번의 비교로 쌍을 찾아야 함
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # left, right 중복처리
                    while left<right and nums[left] == nums[left+1]:
                        left +=1
                    while left<right and nums[right] == nums[right-1]:
                        right -=1
                    left +=1
                    right -=1
                elif nums[i] + nums[left] + nums[right] <0:
                    left +=1
                else:
                    right -=1
        return result

            
            

        