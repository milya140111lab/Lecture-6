# TODO: Вставить сюда код задачи 2.
ts=0
for i in range(n:=int(input())):
    ts+=a if (a:=int(input()))%10==4 and a%6==0 else 0
print(ts)
