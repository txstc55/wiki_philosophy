import random

f=open("Word List copy 3.txt",'r')
q=open("WordList.txt","wr")
lines=f.read().splitlines()
p=random.sample(lines,50000)
for i in p:
    q.write(i+"\n")

f.close()
q.close()