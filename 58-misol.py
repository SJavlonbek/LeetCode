def lengthOfLastWord(s):
    words=s.split()
    if len(words)==0:
        return 0
        
    else:
        last_words=words[-1]
        return len(last_words)

s=input("suz kiriitng:")
print(lengthOfLastWord(s))