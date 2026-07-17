# Finding Equilibrium index in an array
class Solution:
    def sample(self, arr):
        total = sum(arr)
        left = 0
        
        for i in range(len(arr)):
            total -= arr[i]
            
            if left == total:
                return i
            left += arr[i]
        return -1
        
        
        
def main():
    arr = list(map(int, input().split()))
    obj = Solution()
    print(obj.sample(arr))
    
if __name__ == "__main__":
    main()
        