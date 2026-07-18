class Solution:
    def sample(self,s):
        words = s.split()
        ans = ""
        max_repeat = 1
        
        for word in words:
            freq = {}
            
            for ch in word:
                freq[ch] = freq.get(ch,0) + 1
            curr_max = max(freq.values())
            
            if curr_max > max_repeat:
                max_repeat = curr_max
                ans = word
                
        if max_repeat == 1:
            return -1
        return ans
    
def main():
    s = input()

    obj = Solution()
    print(obj.sample(s))


if __name__ == "__main__":
    main()
            