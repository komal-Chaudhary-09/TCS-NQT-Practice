# median of elements of array

class Solution:
    def median(self, arr):
        n = len(arr)
        if n%2 != 0:
            return arr[n//2]
        else:
            return (arr[n//2 - 1] + arr[n//2] /2)
        
def main():
    arr = list(map(int, input().split()))
    obj = Solution()
    print(obj.median(arr))
    
if __name__ ==  "__main__":
    main()