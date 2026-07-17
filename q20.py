# Permutations in which N people can occupy R seats
from math import factorial
class Solution:
    def sample(self, n, r):
        return factorial(n) // factorial(n - r)

def main():
    n, r = map(int, input().split())
    obj = Solution()
    print(obj.sample(n,r))
    
if __name__ == "__main__":
    main()