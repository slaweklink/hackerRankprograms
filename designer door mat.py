n, m = map(int, input().split()) #gets two characters from input


for i in range(1,n,2):
    print((i*".|.").center(m,"-")) # draws the .|. surrounded by -----
print("WELCOME".center(m,"-"))

for  i in range(n-2, -1, -2):
    print((i*".|.").center(m,"-"))
