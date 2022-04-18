# def canPartitionKpart(nums,k):
#     if k==1:
#         return True
#     target,resid=sum(nums)//k,sum(nums)%k
#     if resid!=0:
#         return False
#     nums.sort()
#     if nums[-1]>target:
#         return False
#     while nums and nums[-1]==target:
#         nums.pop()
#         k-=1
#     if k==0 or any(nums):
#         return True
#     return dfs([0]*k,nums,target)

# def dfs(group,nums,target):
#     if not nums:
#         return True
#     v=nums.pop()
#     print("尝试放置数字{}，剩余数组{}".format(v,nums))
#     for i in range(k):
#         if group[i]+v<=target:
#             group[i]+=v
#             print("尝试放置数字{}在位置{},group为{}".format(v,i,group))
#             if dfs(group):
#                 return True
#             print("数字{}放置{}失败，group为{}".format(v,i,group))
#             group[i]-=v
#         if group[i]==0:
#             break
#     nums.append(v)
#     print("数字{}放置失败，nums退回成{} \n-----".format(v,nums))
#     return False

# if __name__ == "__main__":
#     nums=[1,2,3,4,5,6,7,8,9]
#     k=3
#     res=canPartitionKpart(nums,k)
#     print(res)

def canPartitionKpart(nums,k):
    if k==1:
        return True
    target,resid=sum(nums)//k,sum(nums)%k
    if resid!=0:
        return False
    nums=sorted(nums,reverse=True)
    if sum(nums)<target:
        return False
    return dfs(nums,0,[0]*k,target)

def dfs(nums,index,buckets,target):
    if index==len(nums):
        for bucket in buckets:
            if bucket!=target:
                return False
        return True
    for i in range(len(buckets)):
        if buckets[i]+nums[index]>target:
            continue
        buckets[i]+=nums[index]
        if dfs(nums,index+1,buckets,target):
            return True
        buckets[i]-=nums[index]
    return False

if __name__ == "__main__":
    nums=[1,2,3,4,5,6,7,8,9]
    k=2
    res=canPartitionKpart(nums,k)
    print(res)