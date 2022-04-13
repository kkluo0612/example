from sortedcontainers import SortedList

def longestSubarry(nums,limit):
    s=SortedList()
    n=len(nums)
    left=right=ret=0

    while right<n:
        s.add(nums[right])
        while s[-1]-s[0]>limit:
            s.remove(nums[left])
            left+=1
        ret=max(ret,right-left+1)
        right+=1
    return ret

if __name__ == '__main__':
    nums=[8,2,4,7]
    limit=4
    res=longestSubarry(nums,limit)
    print(res)