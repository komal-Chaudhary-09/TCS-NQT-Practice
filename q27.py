# Count number of vowels, consonants, spaces in String
class Solution:
    def sample(self, str):
        vcount = 0
        ccount = 0
        wcount = 0
        str = str.lower()
        
        for ch in str:
            if ch in 'aeiou':
                vcount += 1
            elif ch == " ":
                wcount += 1
            elif 'a' <= ch <= 'z':
                ccount += 1
        return f"vowels: {vcount}\nconsonants: {ccount}\nwhite spcase: {wcount}"
        
def main():
    str = input()
    obj = Solution()
    print(obj.sample(str))
    
if __name__ == "__main__":
    main()
    