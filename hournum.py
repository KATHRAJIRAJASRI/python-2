b=4
count=1
for i in range(1,2*b):
    string=""
    cols=b-i+1 if i<=b else i-b+1
    spaces=i-1 if i<=b else 2*b-i-1
    for sp in range(1,spaces+1):
        string+=" "
    for j in range(1,cols+1):
        string+=str(count)+" "
        count+=1
    print(string)