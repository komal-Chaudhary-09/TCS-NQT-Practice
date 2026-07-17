class Solution:
    def sample(self, arr):
        seen = {}
        result = []
        
        for a,b in arr:
            if (b,a) in seen:
                result.append((a,b))
            else:
                seen[(a,b)] = True
        return result
    
def main():
    arr = list(map(int, input().split()))
    
        
        