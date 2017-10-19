
import csv
from bs4 import BeautifulSoup
import urllib.request
import signal
import cgi

import html.parser


file=open("Categories.csv")
categories=csv.reader(file)

cate=zip(*categories)
cate=categories

#print (categories)
def get_first_category(url):
    k = urllib.request.urlopen(url)
    soup = BeautifulSoup(k)
    t = soup.select('#mw-normal-catlinks ul li a')
    for i in t:
        if i.string=='Living people':
            return ['https://en.wikipedia.org/wiki/Category:Living_people','Living people']
    q=t[0].string
    j=q
    j=j.replace(" ", "_")
    #print(j)
    p = ["https://en.wikipedia.org/wiki/Category:", j]
    return ["".join(p),q]


#print (get_first_category('https://en.wikipedia.org/wiki/Category:Charitable_organizations'))


def find_category(url):
    #print (url)
    k=get_first_category(url)[1]
    #print (k)
    p=[]
    if_return=1
    for i in categories:
        if k in i:
            if_return = 0
            p= [1,i[0]]
    if if_return:
        p=[0, k]
    return p


#print (find_category('https://en.wikipedia.org/wiki/Category:Charitable_organizations'))
#print(find_category('https://en.wikipedia.org/wiki/Category:Fields_of_mathematics'))



def main(url):

    try:
        #print (url)
        if_return=0
        k=get_first_category(url)[1]
        file = open("Categories.csv")
        categories = csv.reader(file)

        categories = zip(*categories)
        for i in categories:
            #print (i)
            if k in i:
                #print (i[0])
                return i[0]
        url=get_first_category(url)[0]
        #print (url)
        #print (url)
        return main(url)
    except  Exception:
        print("No Category")
        return "No Category"


f=open('links.txt','r')
q=open('categories.txt','w')

 

lines=f.read().splitlines()
for i in lines:
    def signal_handler(signum, frame):
        raise Exception("Timed out!")

    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(20) 
    try: 
        print (i)
        q.write(main(i)+"\n")
    except Exception:
        q.write("No Category"+"\n")

f.close()
q.close()