#!/usr/bin/env python3
x=input("enter the text:")
y=len(x)
print(x,"\ncount is:", y)

#q2
f=input("first name:")
l=input("last name:")
print(f,l,"\n",f[0].capitalize(),l[0])

#q3
ans1=x.endswith(".")
ans2=x.isalpha()
ans3="x"in x
print(ans1,"\n",ans2,"\n",ans3)
ne="enter nothing enquire nothing"
print("OLD:",ne)
print(ne.replace("e","E"))

#q4
#first character of the string & num of times it occur
u=input("enter new string:")
print("first character:",u[0],"no. of times it occurs",u.count(u[0]))
#first character of the string & num of times it occur
print("LAST character", u[-1],"COUNT",u.count(u[-1]))




