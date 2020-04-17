s=input()
a=0
d=0
l=0
u=0
t=0
#s=t.replace(" ","")
#print(s)
for i in range(len(s)):
    if (s[i].isalnum())==True:
        t+=1
    if (s[i].isalpha())==True:
        a+=1
    if (s[i].isdigit()) ==True:
        d+=1
    if (s[i].islower()) ==True:
        l+=1
    if (s[i].isupper()) == True:
        u+=1
if (t>0):print("True")
else:print("False")
if (a>0):print("True")
else:print("False")
if (d>0):print("True")
else:print("False")
if (l>0):print("True")
else:print("False")
if (u>0):print("True")
else:print("False")


