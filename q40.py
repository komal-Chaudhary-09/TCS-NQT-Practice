# Find Non-repeating characters of a String
class Solution:
    def sample(self,s):
        freq = {}
        result = ""
        for ch in s:
            freq[ch] = freq.get(ch,0) + 1
            
        
        for key in s:
           if freq[key] == 1:
            result += key
        return result
    
def main():
    s1 = input()
    
    obj = Solution()
    print(obj.sample(s1))
    
if __name__ == "__main__":
    main()
        
    
