num=[0,10,5,4,20,323,45,100,37,73,56,72,39,90,98,87,29]
n=1
while n==1:
    n=0
    for i in range (len(num)-1):
        a=num[i]
        b=num[i+1]
        if a>b:
            num[i]=b
            num[i+1]=a
            n=1
print(num)
