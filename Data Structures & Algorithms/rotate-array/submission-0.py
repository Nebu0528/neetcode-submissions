class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -=1

        n = len(nums)
        #if k > n: use the modulo
        k = k % n

        #reverse the entire array
        reverse(0, n-1)

        #reverse the first k elements
        reverse(0, k-1)

        #reverse after the k elements
        reverse(k, n-1)

        
        