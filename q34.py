# Sum of the Numbers in a String
class Solution:
    def sample (self,s):
        
        
        
        total = 0
        num = ""
        
        for ch in s:
            if ch.isdigit():
                num += ch
            else:
                if num:
                    total += int(num)
                    num = ""
        if num:
            total += int(num)
        return total
    
    
def main():
    s = input()
    obj = Solution()
    print(obj.sample(s))
    
if __name__ == "__main__":
    main()
    