class Solution:
    def rotate(self, arr, k ):
        n = len(arr)
        k %=n
        arr[:k] = reversed(arr[:k])
        arr[k:] = reversed(arr[k:])
        arr.reverse()
        return arr
        
        
def main():
    arr = list(map(int, input().split()))
    k = int(input())
    obj = Solution()
    print(obj.rotate(arr, k ))

if __name__ == "__main__":
    main()
    