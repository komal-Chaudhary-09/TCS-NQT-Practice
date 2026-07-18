# Check if the given String is Palindrome or not
class Solutions:
    def sample(self, str):
        if str == str[::-1]:
            return ("Palindrome")
        return ("Not Plaindrome")
    
def main():
    str = input()
    obj = Solutions()
    print(obj.sample(str))

if __name__ == "__main__":
    main()
        
        
    
        