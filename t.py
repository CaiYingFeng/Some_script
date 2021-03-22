
mylist=[1.2345,0.95,2.3,7,0.5]
mylist2=mylist.copy()
mylist.sort()
index=[]
for i in mylist:
    index.append(mylist2.index(i))

print(mylist)
print(mylist2)
print(index)