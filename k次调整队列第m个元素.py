def transformK(nums,k,m):
    i,j=0,1
    n=len(nums)
    if n<2:
        return
    while k:
        nums[n-1]=nums[i] if nums[i]<nums[j] else nums[j]
        k=k%(n-1)
    return nums[m]

if __name__ == '__main__':
    nums=[3,2,9,0,1,7,6,5,4]
    k=7
    m=0
    print(transformK(nums,k,m))