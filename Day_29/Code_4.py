def palindrome(s):
    i=0
    n=len(s)
    j=n-1

    while i<j:
        if (s[i]!=s[j]):
            return False
        i+=1
        j-=1

    return True
ans=palindrome("abbass")
print(ans)