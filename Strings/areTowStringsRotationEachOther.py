s1 = "abcde"
s2 = "abced"


def areRotations(s1, s2):
    if len(s1) != len(s2):
        return False
    if s1 == "" and s2 == "":
        return True
    temp = s1 + s1
    n = len(s2)
    temp2 = temp[0:n]
    while n < len(temp):
        if temp2 == s2:
            return True
        else:
            temp2 = temp2[1:] + temp[n]
            n += 1
    return False


print(areRotations(s1, s2))
