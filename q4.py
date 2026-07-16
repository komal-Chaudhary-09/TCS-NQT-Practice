# Reverse a given array
arr = list(map(int, input().split()))
n = len(arr)
result = []

for i in range (n-1, -1 , -1):
    result.append(arr[i])
print(result)