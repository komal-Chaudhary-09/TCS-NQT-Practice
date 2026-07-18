# Remove all vowels from the String
class Solution:
    def sample(self, s):
        result = ""
        for ch in s:
            if ch  not in 'aeiou':
                result += ch
        return result
    
def main():
    s = input()
    obj = Solution()
    print(obj.sample(s))
    
if __name__ == "__main__":
    main()
        