from typing import List

# List.sort()
def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    lenth = len(nums)
    ans = []

    for i in range(0,lenth):
        if i>0 and nums[i] == nums[i-1]:
                continue
        k = lenth-1

        for j in range(i+1, lenth):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue

                while j<k and nums[i] + nums[k] +nums[j] >0:
                    k-=1

                if j == k:
                    break

                if nums[i] + nums[k] +nums[j] ==0:
                    ans.append([nums[i],nums[j],nums[k]])
                
    return ans

if __name__ =='__main__':
    print(threeSum([-1,0,1,2,-1,-4]))