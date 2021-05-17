s1 = "geeksforgeeks"
s2 = "krrek"


def isValidSubsequence(s1, s2):
    i, j = 0, 0

    while i < len(s1):
        if s1[i] == s2[j]:
            i += 1
            j += 1
            if j == len(s2)-1:
                return True
        else:
            i += 1
    return False

print(isValidSubsequence(s1, s2))
