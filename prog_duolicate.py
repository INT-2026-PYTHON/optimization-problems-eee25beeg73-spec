x=int(input("enter the number of elements:"))
l=[]
for i in range(x):
    n=int(input("enter the number:"))
    l.append(n)
def has_duplicate_brute(nums):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]==nums[j]:
                return 'true'
    return 'false'
def has_duplicate_fast(nums):
    seen=[]
    for i in nums:
        if i in seen:
            return 'true'
        else:
            seen.append(i)
    return 'false'
print("brute force:",has_duplicate_brute(l))
print("optimized:",has_duplicate_fast(l))
