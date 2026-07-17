# Find the sum of numbers in the given range
class Solution:
    def sample(self, l, r):
        sum = 0
        current = l
        n = r - l + 1
        for i in range(n):
            sum  = sum +current
            current += 1
        return sum
    
def main():
    l = int(input())
    r = int(input())
    obj = Solution()
    print(obj.sample(l,r))

if __name__ == "__main__":
    main()
        
        