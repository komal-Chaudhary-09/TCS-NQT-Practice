# Remove All Duplicates from a String
class Solution:
    def sample(self, s):
        result = ""
        seen = set()
        
        for ch in s:
            if ch not in seen:
                seen.add(ch)
                result += ch
                
        return result
def main():
    s = input()
    obj = Solution()
    print(obj.sample(s))
    
if __name__ == "__main__":
    main()
            