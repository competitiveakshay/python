word1 = str(input("Enter word1: "))
word2 = str(input("Enter word2: "))

A,B = len(word1), len(word2)
a,b = 0,0
ans = []

word = 1
while a<A and b<B:
    if word==1:
        ans.append(word1[a])
        a += 1
        word = 2
    if word==2:
        ans.append(word2[b])
        b += 1
        word = 1
    
while a<A:
    ans.append(word1[a])
    a += 1

while b<B:
    ans.append(word2[b])
    b += 1

final = "".join(ans)
print(final)
