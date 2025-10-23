l2 = [7, 'zebra', 'apple', 10, 'yellow', 'blue', 4, 'x_ray', 'dog', 1, 'white', 'maroon', 9, 'violet', 'green', 3, 'pink', 'horse', 5, 'island', 'orange', 2, 8, 6, 180, 1024, 29, 270, 2134]

nums = []
for i in range(len(l2)):
    if type(l2[i]) is int:
        nums.append(l2[i])
for i in range(len(l2)):
    print(i)
    if type(l2[i]) is int:
        l2.remove(l2[i])
print(l2)
print(nums)
l2 = sorted(l2)
nums = sorted(nums)
l2.extend(nums)
print(l2)