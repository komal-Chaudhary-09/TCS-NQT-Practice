# Remove Spaces from a String
class Solution:
    def sample(self, s):
        result = ""
        for ch in s:
            if ch != " ":
                result += ch
        return result

def main():
    s = input()
    obj = Solution()
    print(obj.sample(s))
    
if __name__ == "__main__":
    main()