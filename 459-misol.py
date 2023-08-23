def repeatedSubstringPattern(s: str) -> bool:
    
    for j in range(1, len(s)):
        if s[0] == s[j]:
            x = ""
            for i in range(j):
                x += s[i]
                   
            if s.replace(x, "") == "":
                return True
    return False

print(repeatedSubstringPattern("abcabcabcabc"))
print(repeatedSubstringPattern("abab"))
print(repeatedSubstringPattern("aba"))