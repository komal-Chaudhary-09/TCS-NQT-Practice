# Average of all elements in an array
class Solution:
    def average(self, arr):
        n = len(arr)
        avg = 0
        sum = 0
        for i in range(n):
            sum += arr[i]
        return sum / n;
    
def main():
    arr = list(map(int, input().split()))
    obj = Solution()
    print(obj.average(arr))
if __name__ == "__main__":
    main()