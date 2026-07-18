# Print all the duplicates in the string
class Solution:
    def sample(self,s):
        freq = {}
        result = []
        
        for ch in s:
            freq[ch] = freq.get(ch,0)+1
            
        for ch in freq:
            if freq[ch] > 1:
                result.append(f"{ch}: {freq[ch]}")
        return "[" + ",".join(result) +"]"
    
def main():
    s = input()
    obj = Solution()
    print(obj.sample(s))
    
if __name__ == "__main__":
    main()
                