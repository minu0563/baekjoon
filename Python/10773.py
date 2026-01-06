a = int(input())
nums = []
b = 0

for i in range(a):
    num = int(input())
    if num != 0:
        nums.append(num)
    elif num == 0:
        nums.pop()

for i in range(len(nums)):
    b += nums[i]
    
print(b)