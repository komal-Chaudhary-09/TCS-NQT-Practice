# Calculate Frequency of characters in a String
class Solution:
    def sample(self,s):
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch,0) +1
        for ch in sorted(freq):
            print(ch, freq[ch], sep = "")
            
            
        
def main():
    s = input()
    obj = Solution()
    obj.sample(s)
    
if __name__ == "__main__":
    main()