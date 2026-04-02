class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # 입력 배열 양 끝에 포인터 생성 
        # 결과 담을 배열 초기화 -> 크기는 nums랑 같음
        # 인덱스로 삼을 변수 초기화
        # 배열 순회
        # -> 절댓값 제곱 시 더 큰 쪽을 결과 배열에 담고 인덱스 이동

        left = 0
        right = len(nums)-1
        result = [0] * len(nums)
        idx = len(nums) -1 # result 배열의 인덱스

        while left <= right:
            if abs(nums[left]) < abs(nums[right]):
                result[idx] = nums[right]**2
                idx -=1
                right-=1
            else:
                result[idx] = nums[left]**2
                idx -=1
                left+=1
        return result