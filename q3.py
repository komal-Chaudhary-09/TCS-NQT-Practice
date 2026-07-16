# Second Smallest and Second Largest element in an array

arr = list(map(int, input().split()))
small = min(arr)
large = max(arr)

second_small = float('inf')
second_large = float('-inf')

for num in arr:
    if num > small and num < second_small:
        second_small = num
for num in arr:
    if num > second_large and num < large:
        second_large = num
print(second_small)
print(second_large)