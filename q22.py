class Solution:
    def sample(self, arr1, arr2):
        s = set(arr2)
        for i in arr1:
            if i not in s:
                return False
        return True
    
def main():
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    obj = Solution()
    print(obj.sample(arr1, arr2))
    
if __name__ == "__main__":
    main()
    
        
        