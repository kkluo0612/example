def numOfSubarrays(nums):
    mod=10**9+7
    odd,even=0,1  #奇数和偶数的子数组数目
    subarrays=0
    total=0

    for num in nums:
        total+=num
        if total%2==0:
            even+=1
            subarrays+=odd
        else:
            odd+=1
            subarrays+=even
        # if total%2==0:
        #     even+=1
        # else:
        #     odd+=1
    return subarrays%mod

if __name__ == '__main__':
    nums=[1,3,5]
    print(numOfSubarrays(nums))