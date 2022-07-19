# LeetCode : (4) Median of Two Sorted Arrays (hard)

# Not in expected Time(O(log(m+n))), kind of bruteforce solution but 93% faster than other python submissions.
def findMedianSortedArrays( nums1, nums2) -> float:
    nums1 =  nums1 + nums2
    nums1.sort()
    n = len(nums1)
    
    if n % 2 != 0:
        mid = nums1[n//2]
        return mid
    elif n%2 == 0:
        mid = n//2
        avg = (nums1[mid] + nums1[mid-1]) /2
    return avg

# Driver code

nums1 = [1,2]
nums2 = [3,4]
print(findMedianSortedArrays(nums1, nums2))

#  Time complexity : O(n log n)
# Space complexity : O(1)