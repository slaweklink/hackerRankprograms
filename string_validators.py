slowo = input()
countalnum = 0
countalpha = 0
countdigit = 0
countlower = 0
countupper = 0
for letter in slowo:
    if letter.isalnum():
        countalnum += 1
for letter in slowo:
    if letter.isalpha():
        countalpha += 1
for letter in slowo:
    if letter.isdigit():
        countdigit += 1
for letter in slowo:
    if letter.islower():
        countlower += 1
for letter in slowo:
    if letter.isupper():
        countupper += 1

if countalnum > 0:
    print("True")
else:
    print("False")

if countalpha > 0:
    print("True")
else:
    print("False")

if countdigit > 0:
    print("True")
else:
    print("False")

if countlower > 0:
    print("True")
else:
    print("False")

if countupper > 0:
    print("True")
else:
    print("False")

