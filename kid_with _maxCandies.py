# LeetCode: (1431) Kids With the Greatest Number of Candies (Easy)

def kidsWithCandies( candies, extraCandies: int) -> bool:
    ans=[]*len(candies)
    max_candies=0
    
    
    for i in range(len(candies)):
        max_candies= candies[i]+ extraCandies
        if (max_candies>= max(candies)):
            ans.append(True)
        else:
            ans.append(False)
    return ans

# Driver code
candies= [2,3,5,1,3]
extraCandies = 3

print(kidsWithCandies(candies,extraCandies))