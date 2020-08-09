class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '' or haystack == needle:
            return 0

        if len(haystack) >= len(needle):
            for i in range(len(haystack)):
                flag = True
                if haystack[i] == needle[0]:
                    n = i
                    for j in range(len(needle)):
                        if n >= len(haystack) or haystack[n] != needle[j]:
                            flag = False
                            break
                        n += 1

                    if flag:
                        return i
                    elif len(haystack) - i < len(needle):
                        return -1
                
        return -1