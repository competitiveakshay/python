# a = 100

# def hello():
#     a = 500
#     print(a)

# hello()
# print(a)


a = 100

def hello():
    global a
    a = 500
    b = 10
    print(a)

hello()
print(a)
# print(b) b