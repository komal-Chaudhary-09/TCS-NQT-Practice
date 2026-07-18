# Capitalize first and last character of each word of a string
class Solution:
    def sample (self, s):
        words = s.split()
        result = []
        
        for word in words:
            if len(word) == 1:
                result.append(word.upper())
            else:
                word = word[0].upper() + word[1:-1] + word[-1].upper()
                result.append(word)
        return " ".join(result)
    
  
def main():
    s = input()
    obj = Solution()
    print(obj.sample(s))

if __name__ == "__main__":
    main()     
            
        
        
        
        
        
        
        
        
