# Remove brackets from an algebraic expression

def sample (s):
     
     s = s.replace("(", "")
     s = s.replace(")", "")
     return s
s = input()
print(sample(s))