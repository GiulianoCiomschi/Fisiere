f=open("C:\\Users\\admin\\Downloads\\Lista clasei 11D.txt",'r')
l=list(f)
f.close()
n=medie=0

x=open('C:\\Users\\admin\\Desktop\\Lista clasei 11 D Eng_1.txt', 'w')
y=open('C:\\Users\\admin\\Desktop\\Lista clasei 11 D Eng_2.txt', 'w')
for i in l:
    a=i.split()
    nota=int(a[2])
    n+=1
    medie+=nota
    if a[3]=='Eng_1':
        x.write(a[0]+' '+a[1]+' '+a[2])
        x.write('\n')
    else:
        y.write(a[0]+' '+a[1]+' '+a[2])
        y.write('\n')
x.close()
y.close()

g=open("C:\\Users\\admin\\Desktop\\Media.txt","w")
g.write('Media totala a elevilor la limba engleza este:')
g.write(str(round(medie/float(n),2)))
g.close()
