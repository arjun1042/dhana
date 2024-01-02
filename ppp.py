n=int(input())
k=int(input())
mon=[]
for i in range(n):
    mon.append(int(input()))
mi=min(mon)
ma=ma-k
mi=mi+k
diff=ma-mi
print(diff)
