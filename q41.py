# Check if two Strings are anagrams of each other
class Solution:
    def sample(self,s1, s2):
        return sorted(s1) == sorted(s2)
        
def main():
    s1 = input()
    s2 = input()
    
    obj = Solution()
    print(obj.sample(s1,s2))
    
if __name__ == "__main__":
    main()