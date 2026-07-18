# Remove characters from a string except alphabets
class Solution:
    def sample(self,s):
        result = ""
        
        for ch in s:
            if ('a' <= ch <= 'z') or ('A' <= ch <=  'Z'):
                result += ch
        return result
    
def main():
    s = input()
    obj = Solution()
    print(obj.sample(s))
    
if __name__ == "__main__":
    main()
        