# Find all non-repeating elements in an array
from collections import Counter

def sample(arr):
    count = Counter(arr)
    result = []
    
    for element in arr:
        if count[element] == 1 :
            result.append(element)
    return result

def main():
    arr = list(map(int, input().split()))
    print(sample(arr))
if __name__ == "__main__":
    main()