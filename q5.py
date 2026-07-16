# Rearrange array in increasing-decreasing order

class Solution:
    def rearrange(self, arr):
        result = []
        arr.sort()
        p = len(arr)
        n = (p+1)//2
        
        for i in range(n):
            result.append(arr[i])
        for j in range(p-1, n-1, -1):
            result.append(arr[j])
        return result

def main():
    arr = list(map(int, input().split()))
    obj = Solution()
    print(obj.rearrange(arr))
if __name__ =="__main__":
    main()
        
            
            
            
        