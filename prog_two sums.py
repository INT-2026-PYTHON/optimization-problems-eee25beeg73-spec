x=int(input("enter the number of elements:"))
l=[]
for i in range(x):
    n=int(input("enter the number:"))
    l.append(n)
def two_sum_brute(nums,target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target and i<j:
                return (i,j)
def two_sum_fast(nums,target):
    d={}
    for i in range(len(nums)):
        c=target-nums[i]
        if c in d:
            return(d[c],i)
        else:
            d[nums[i]]=i
t=int(input("enter the target:"))
print("brute force:",two_sum_brute(l,t))
print("optimized:",two_sum_fast(l,t))