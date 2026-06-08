x=int(input("enter the number of elements:"))
l=[]
for i in range(x):
    n=int(input("enter the number:"))
    l.append(n)
def count_pairs_brute(nums,target):
    count=0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i]+nums[j]==target and nums[i]<nums[j]:
                count +=1
    return count
def count_pairs_fast(nums,target):
    freq={}
    count=0
    for i in nums:
        c=target-i
        if c  in freq:
            count += freq[c]
        freq[i]=freq.get(i,0)+1
    return count
t=int(input("enter the target:"))
print("brute force:",count_pairs_brute(l,t))
print("optimised:",count_pairs_fast(l,t))
