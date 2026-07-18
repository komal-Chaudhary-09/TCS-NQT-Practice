# Change every letter with next lexicographic alphabet
class Solution:
    def sample(self,s):
        result = ""
        
        for ch in s:
            if ch == 'z':
                result += 'a'
            else:
                result += chr(ord(ch) + 1)
        
def main():
    s = input()
    obj = Solution()
    print(obj.sample(s))
    
if __name__ == "__main__":
    main()