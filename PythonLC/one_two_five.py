class Solution:
    def isPalindrome(self, s) -> bool:
        s = s.lower()
        a = 0
        b = len(s) - 1
        while a <= b:
            if ord(s[a]) > ord('z') or ord(s[a]) < ord('a'):
                a += 1
                continue
            if ord(s[b]) > ord('z') or ord(s[b]) < ord('a'):
                b -= 1
                continue
            if s[a] != s[b]:
                return False
            a += 1
            b -= 1
        return True

A = Solution()
print(A.isPalindrome('A man, a plan, a canal: Panama'))