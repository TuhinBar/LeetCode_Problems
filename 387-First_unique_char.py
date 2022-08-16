# LeetCode No: 387 - First Unique Character in a String  https://leetcode.com/problems/first-unique-character-in-a-string/
import collections 

def firstUniqChar( s: str) -> int:
        hashtable = collections.Counter(s)
        for i in s:
            if hashtable[i] == 1:
                return s.index(i)
        return -1

# Test
s = "leetcode"
print(firstUniqChar(s))

# Time Complexity: O(n)
# Space Complexity: O(n)