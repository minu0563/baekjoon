import sys
input=sys.stdin.readline
nums={}
for _ in range(int(input())):
  num=int(input())
  try:
    nums[num]+=1
  except:
    nums[num]=1
nums=sorted(nums.items())
for i,j in nums:
  for _ in range(j):
    print(i)