class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 정렬
        nums1.sort()
        nums2.sort()
        result = []
        i,j = 0,0
        # 포인터 이동하면서 비교
        while(i < len(nums1) and j < len(nums2)):
            if nums1[i] == nums2[j]:
                if nums1[i] not in result: # 결과값이 unique 이도록
                    result.append(nums1[i])
                i+=1
                j+=1
            elif nums1[i] < nums2[j]:
                i+=1
            else:
                j+=1
        return result