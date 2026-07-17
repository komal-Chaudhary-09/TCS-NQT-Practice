class Solution:
    def final (self, arr):
        sample = sorted(arr)
        rank = {}
        current_rank = 1
        
        for num in sample:
            if num not in rank:
                rank[num] = current_rank
                current_rank += 1
        result = []
        
        for num in arr:
            result.append(rank[num])
        return result
def main():
    arr = list(map(int, input().split()))
    obj = Solution()
    print(obj.final(arr))
    
if __name__ == "__main__":
    main()
                
            
            
            