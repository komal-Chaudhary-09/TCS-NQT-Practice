# Program to Add two fractions
from math import gcd
class Solution:
    def sample(self,a,b,c,d):
        nume = (a*d)+(c*b)
        deno = (b*d)
        g = gcd(nume,deno)
        nume //= g
        deno //= g
        return (nume,deno)
def main():
    a, b, c, d = map(int, input().split())
    obj = Solution()
    print(*obj.sample(a,b,c,d))
if __name__ == "__main__":
    main()