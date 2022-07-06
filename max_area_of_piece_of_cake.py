# Leetcode: 1465 - Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts

# Bruteforce 

def maxArea( h, w, horizontalCuts, verticalCuts):
    hCuts=horizontalCuts
    vCuts=verticalCuts
    hCuts.sort()
    vCuts.sort()
    cakeSize_hCut=0
    cakeSize_vCut=0
    for i  in range(len(hCuts)):
        if i==0:
            diff_hCut=abs(hCuts[i]-0)
            cakeSize_hCut=max(cakeSize_hCut,diff_hCut)
        if i!=len(hCuts)-1:
            diff_hCut=abs(hCuts[i]-(hCuts[i+1]))
            cakeSize_hCut=max(cakeSize_hCut,diff_hCut)
        else:
            diff_hCut=abs(hCuts[i]-h)
            cakeSize_hCut=max(cakeSize_hCut,diff_hCut)
    for j in range(len(vCuts)):
        if j==0:
            diff_vCut=abs(vCuts[j]-0)
            cakeSize_vCut=max(cakeSize_vCut,diff_vCut)
        if j!=len(vCuts)-1:
            diff_vCut=abs(vCuts[j]-(vCuts[j+1]))
            cakeSize_vCut=max(cakeSize_vCut,diff_vCut)
        else:
            diff_vCut=abs(vCuts[j]-w)
            cakeSize_vCut=max(cakeSize_vCut,diff_vCut)
    return (cakeSize_hCut * cakeSize_vCut)%((10**9)+7)


# DRIVER    Code

h=5
w=4
horizontalCuts= [3]
verticalCuts=[3]
print(maxArea(h,w,horizontalCuts,verticalCuts))


# Optimal
def maxArea( h, v, hCuts, vCuts) -> int:
        h,v=0,0
    
        for i in range(1,len(hCuts)):
            v = max( v , hCuts[i] - hCuts[i-1])

        for j in range(1,len(vCuts)):
            h = max( h , vCuts[j-1])

        return (h*v)%(10**9+7)
