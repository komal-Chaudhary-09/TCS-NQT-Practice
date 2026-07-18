# Remove Characters from first String present in the Second String
def sample(s1,s2):
    result = ""
    remove = set(s2)
    
    for ch in s1:
        if ch not in remove:
            result += ch
            
    return result

def main():
    s1 = input()
    s2 = input()
    print(f'"{sample(s1,s2)}"')
    
if __name__ == "__main__":
    main()
          