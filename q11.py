# Remove Duplicates From an Unsorted Array

class Solution:
    def sample(self, arr):
        seen = {}
        result = []
        
        for val in arr:
            if val not in seen:
                result.append(val)
                seen[val] = True
        return result
    
def main():
    arr = list(map(int, input().split()))
    obj = Solution()
    print(obj.sample(arr))
if __name__ == "__main__":
    main()
            
                
            
        
    
        