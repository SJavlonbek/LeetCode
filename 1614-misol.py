def maxLengthBetweenEqualCharacters( s: str) -> int:
    a=-1
    for i in range(len(s)-1):
        for j in range(i+1,len(s)):
            if s[i]==s[j]:
                if j-i>1:
                    a=max(a,j-i-1)
                else:
                    a=0
                break
    return a
       
print(maxLengthBetweenEqualCharacters("abca"))