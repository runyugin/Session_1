

arr1 = ["hello", "2", "world", ":-)"]
arr2 = []
count = 0

for i in range(len(arr1)):
    if len(arr1[i])<=3:
        arr2.insert(count, arr1[i])
        count+=1

print(*arr2)