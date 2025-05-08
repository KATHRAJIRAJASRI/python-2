a=5
for i in range(1,a+1):
    str=""
    for j in range(1,a+1):
        if j==1 or j==a or i==j:
            str+="*"+" "
        else:
            str+=" "+" "
    print(str)
b=5
for i in range(1,b+1):
    str=""
    for j in range(1,b+1):
        if i==1 or i==b or i+j==b+1:
            str+="*"+" "
        else:
            str+=" "+" "
    print(str)
c=5
mid=a//2+1
for i in range(1,c+1):
    str=""
    for j in range(1,c+1):
        if i<=mid:
            if i==1 or i==mid or j==1 or j==c:
                str+="*"+" "
            else:
                str+=" "+" "
        else:
            if j==1 or i==j:
                str+="*"+" "
            else:
                str+=" "+" "
    print(str)