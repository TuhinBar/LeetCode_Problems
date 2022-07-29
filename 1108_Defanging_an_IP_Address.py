# LeetCode : (1108) Defanging an IP Address - Easy - https://leetcode.com/problems/defanging-an-ip-address/

# Solution:
def defangIPaddr(address) -> str:
    address= address.replace(".","[.]")
    return address

# Driver code
address = "1.1.1.1"
print(defangIPaddr(address))