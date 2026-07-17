# Maximum Product Subarray in an Array
class Solution:
    def sample(self, arr):
        n = len(arr)

        prefix = 1
        suffix = 1
        ans = arr[0]

        for i in range(n):

            if prefix == 0:
                prefix = 1

            if suffix == 0:
                suffix = 1

            prefix *= arr[i]
            suffix *= arr[n - 1 - i]

            ans = max(ans, prefix, suffix)

        return ans


def main():
    arr = list(map(int, input().split()))
    obj = Solution()
    print(obj.sample(arr))

if __name__ == "__main__":
    main()