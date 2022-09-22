# LeetCode: 557 - Reverse Words in a String III  https://leetcode.com/problems/reverse-words-in-a-string-iii/

# Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

# Example 1:
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Note: In the string, each word is separated by single space and there will not be any extra space in the string.

# Time Complexity: O(n)
# Space Complexity: O(n)

# Optimized: O(n) time and O(1) space
def reverseWords(s: str) -> str:
    return " ".join([x[::-1] for x in s.split(" ")])

# Alternative: O(n) time and O(1) space
def reverseWords(s: str) -> str:
    words = s.split(" ")
    for i in range(len(words)):
        words[i] = words[i][::-1]
    return " ".join(words)

# Test
s = "Let's take LeetCode contest"
print(reverseWords(s))
