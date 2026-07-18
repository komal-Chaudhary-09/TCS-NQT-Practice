# Reverse Words in a String
class Solution:
    def sample (self, s):
        arr = s.split()
        
        return " ".join(arr[::-1])
        
def main():
    s = input()
    obj = Solution()
    print(obj.sample(s))
    
if __name__ == "__main__":
    main()