a=4
count=1
for i in range(1,2*a):
    strings=""
    cols=i if i<=a else 2*a-i
    space=a-i if i<=a else i-a
    for sp in range(1,space+1):
        strings+=" "
    for j in range(1,cols+1):
        strings+=str(count)+" "
        count+=1
    print(strings)

    