num=int(input("enter the number:"))
sum=0
temp=num
count=len(str(num))
while temp>0:
    digit=temp%10
    sum+=digit**count
    temp//=10
if num==sum:
    print("num is armstrong")
else:
    print("num is not armstrong")        