# Find the largest word in a String
def large(s):
    words = s.split()
    max_length = 0
    ans = ""
    
    for word in words:
        length = len(word)
        
        if length > max_length:
            max_length = length
            ans = word
    return ans 

s = input()
print(large(s))
        
    