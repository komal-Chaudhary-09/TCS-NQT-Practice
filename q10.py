# Remove duplicates from a sorted array
class Solution:
    def noduplicate(self,arr):
        n = len(arr)
        if n == 0:
            return []
        i = 0
        for j in range(1,n):
            if arr[i] != arr[j]:
                i += 1
                arr[i] = arr[j]
        return arr[: i+1]
            
            
            
            
            
            
def main():
    arr = list(map(int, input().split()))
    obj = Solution()
    print(obj.noduplicate(arr))
if __name__ == "__main__":
    main()