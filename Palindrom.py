#Program to check palindrom
def Palindrom(string):
    return(string == string[::-1])

s = (input("Enter your text:"))

ans = Palindrom(s)

if (ans):
    print("yes string is a palindrom")
else:
    print("string is not a palindrom")