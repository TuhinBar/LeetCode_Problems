# Leetcode: 1047. Remove All Adjacent Duplicates In String
# link: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

def removeDuplicates( s: str) -> str:
    res = []
    for c in s:
        if res and res[-1] == c:
            res.pop()
        else:
            res.append(c)
    return "".join(res)

# Driver code
s = "abbaca"
print(removeDuplicates(s))