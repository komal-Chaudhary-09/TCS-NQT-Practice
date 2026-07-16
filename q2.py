# Find the largest number in an array

arr = list(map(int,input().split()))
largest = arr[0]

for i in range (1, len(arr)):
    if arr[i] > largest:
        largest = arr[i]
print (largest)