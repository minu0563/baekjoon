a = input().lower()
nums = {}

for i in range(len(a)):
    for x in a:
        try:
            nums[x] += 1
        except:
            nums[x] = 1
nums = sorted(nums.items())
for i, j in nums:
    for _ in range(j):
        print(i.upper())
        break
    break