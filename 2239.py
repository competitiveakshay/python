nums = list(map(int, input().split()))

closest = nums[0]
for x in nums:
    if abs(x) < abs(closest):
        closest = x

if closest<0 and abs(closest) in nums:
    print(abs(closest))
else:
    print(closest)