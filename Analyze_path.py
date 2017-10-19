import csv

c=open('result.csv','r')
f=csv.reader(c)
q=[]
for i in f:

    if not i[0]=="":
        i=filter(lambda name: name.strip(), i)
        if len(i)>1 and i[-1]=='Philosophy':
            q.append(i)
s=set()
for i in range (1,10):
    for path in q:
        if len(path)>=i:
            s.add(tuple(path[len(path)-i:len(path)]))
            #print i


q=open('path_analysis.csv','w')

write=csv.writer(q)

#write.writerow(['Source','Target'])
for i in s:
    for j in range(0,len(i)-1):
        write.writerow([i[j],i[j+1]])
    #write.writerow(['a','b'])
    print str(i).strip("()",)



#p=open('path_analysis.csv','wr')

