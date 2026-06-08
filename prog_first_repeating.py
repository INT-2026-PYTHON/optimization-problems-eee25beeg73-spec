x=int(input("enter the number of elements:"))
l=[]
for i in range(x):
    n=int(input("enter the number:"))
    l.append(n)
def first_repeating_brute(nums):
    for i in range(len(nums)):
        for j in range(i):
            if nums[i]==nums[j]:
                return nums[j]
    return -1
def first_repeating_fast(nums):
    seen=[]
    for i in nums:
        if i in seen:
            return i
        else:
            seen.append(i)
    return -1
print("first repeating brute force:",first_repeating_brute(l))
print("first occurance fast:",first_repeating_fast(l))
