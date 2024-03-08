class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        overlap = set(nums1) & set(nums2)
        only_in_1 = set(nums1) - overlap
        only_in_2 = set(nums2) - overlap

        answer = []
        answer.append(list(only_in_1))
        answer.append(list(only_in_2))
        return answer

