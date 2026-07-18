class Solution:
    def sample(self,s):
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch,0) + 1
            
        maxfreq = 0
        maxchar = ""
        
        for ch in freq:
            if freq[ch] > maxfreq:
                maxfreq = freq[ch]
                maxchar = ch
        return maxchar
                
        
def main():
    s = input()
    
    obj = Solution()
    print(obj.sample(s))
    
if __name__ == "__main__":
    main()