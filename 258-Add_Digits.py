# LeetCode No: 258 - Add Digits  https://leetcode.com/problems/add-digits/

def addDigits( num: int) -> int:
        while num>=10:
            num = sum(int(i) for i in str(num))
        return int(num)

# Test
print(addDigits(38))

# Time Complexity: O(1)
# Space Complexity: O(1)