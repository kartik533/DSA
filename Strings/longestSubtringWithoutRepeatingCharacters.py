s = "abcdefghhdaebcgfhd"

def longestSubstringWithoutRepeatingCharacters(s):
    i,j,ans = 0,0,0
    n = len(s)
    unique = set()
    while i<n and j<n:
        if s[j] in unique:
            unique.remove(s[i])
            i += 1
        else:
            unique.add(s[j])
            j += 1
            ans = max(ans, j-1)

    return ans