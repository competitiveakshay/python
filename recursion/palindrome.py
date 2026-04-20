word = str(input("Enter a String: "))
n = len(word)
a,b = 0,n-1

def palindrome(a,b):
    if a>=b:
        return True
    if word[a]!=word[b]:
        return False
    return palindrome(a+1, b-1)

print(palindrome(a,b))