# Calculate sum of the elements of the array
class Solution:
    def sum(self, arr):
        sum = 0
        n = len(arr)
        
        for i in range(n):
            sum += arr[i]
        return sum

def main():
    arr = list(map(int, input().split()))
    obj = Solution()
    
    print(obj.sum(arr))
if __name__ == "__main__":
    main()
    