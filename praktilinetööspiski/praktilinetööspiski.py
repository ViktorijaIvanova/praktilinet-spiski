from random import*
#4
arvud=[]
kogus=int(input("kogus:"))
for i in range(kogus):
    arvud.append(randint(1,100))

#3
arvud=[]
kogus=int(input("kogus: "))
for i in range(kogus):
    arvud.append(randint(-100,100))
    print(arvud)
    max_arv=max(arvud)
    ind=arvud.index(max_arv)
    print(ind)
    print(max_arv)
max_arv=max_arv/kogus
arvud.insert(ind,max_arv)
arvud.pop(ind+1)
print(arvud)





#2
maakonnad=["Tln","Narva","K-Järve","Ida-Virumaa","Tartu","Tartumaa","Viljandi","Pärnumaa"]
osa1=[] 
osa2=[] 
if len(maakonnad)%2==0 and len(maakonnad)>=2:
    n=int(len(maakonnad)/2)
    for i in range(1,n+1):
        osa1.append(maakonnad[i-1])
    for j in range(n+1, len(maakonnad)+1):
        osa2.append(maakonnad[j-1]) 
        osa1.reverse()
        osa2.reverse()
        osa2.extend(osa1)
        print(osa2)
else:
    print("viga!")


#indeks 1
index=""
maakonnad=["Tln","Narva","K-Järve","Ida-Virumaa","Tartu","Tartumaa","Viljandi","Pärnumaa","Saaremaa"]
while True:
    try:
        index=int(input("sisetage indeks: "))
        if index<99999 and index>10000:
            break
    except:
        print("sisetage õige index!")
i=index//10000
print(f"{index} on {maakonnad[i-1]}")
if i in [1,2,3]:
    print("Jääta kodus!")
else:
    print("Kanna maski!") 
