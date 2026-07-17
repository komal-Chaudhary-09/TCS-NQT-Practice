class Solution:
    def sample(self, arr, target):
        
        for i in range (len(arr)):
            if arr[i] == target:
                return i
        return -1
def main():
    arr = list(map(int, input().split()))
    target = int(input())
    obj = Solution()
    
    print(obj.sample(arr, target))

if __name__ == "__main__":
    main()
    