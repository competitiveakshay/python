arr = list(map(int, input().split()))
n = len(arr)
a,b = 0,n-1

def reverse(a,b):
    if a>=b:
        return
    
    arr[a],arr[b] = arr[b],arr[a]
    return reverse(a+1,b-1)

reverse(a,b)
print(arr)
