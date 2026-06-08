x=int(input("enter the number of elements:"))
l=[]
for i in range(x):
    n=int(input("enter the number:"))
    l.append(n)
def has_pair_brute(nums,k):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if abs(nums[i]-nums[j]==k):
                return 'true'
    return 'false'
def has_pair_fast(nums,k):
    c=nums
    for i in nums:
        if (x+k) in c or (x-k) in c:
            return 'true'
    return 'false'
k=int(input("enter the difeerence:"))
print("brute force:",has_pair_brute(l,k))
print("optimised:",has_pair_fast(l,k))