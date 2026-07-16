# insertion at end
def insertAtBeginning(arr, x):
    arr.insert(0,x)
    return arr
arr = list(map(int, input().split()))
x = int(input())
print(insertAtBeginning(arr,x))

#  insertion at end 
# arr.insert(x)

#  insertion at specific position 
# arr.insert (pos,x)