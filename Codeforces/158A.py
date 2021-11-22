n, k = map(int, input().split())
nums = list(map(int, input().split()))
kth = nums[k-1]

cons = 0
for i in nums:
    if i >= kth and i != 0:
        cons += 1
    else:
        break

print(cons)
