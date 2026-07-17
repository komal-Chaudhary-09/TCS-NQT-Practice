# Sort Elements of an Array by Frequency
from collections import Counter
class Solution:
    def sample(self, arr):
        count = Counter(arr)
        
        return sorted(arr, key = lambda x: (-count[x], x))
    
def main():
    arr = list(map(int, input().split()))
    obj = Solution()
    
    print(obj.sample(arr))
    
if __name__ == "__main__":
    main()
    
            