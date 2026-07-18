# Find the ASCII value of a character
class Solution:
    def sample (self, s):
        return ord(s)
        
def main():
    s = input()
    obj = Solution()
    print(obj.sample(s))
    
if __name__ == '__main__':
    main()
    