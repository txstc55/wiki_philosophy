#!/usr/bin/python
# -*- coding: utf-8 -*-

import signal
import urllib2
import re
import cgi
from  BeautifulSoup import BeautifulSoup

web_opener = urllib2.build_opener()
web_opener.addheaders = [('User-agent', 'Mozilla/5.0')]

template = "https://en.wikipedia.org/wiki/"

def getFirstLink(url):
	webpage = web_opener.open(url).read()
	parsed_webpage = BeautifulSoup(webpage)
	paragraphs = parsed_webpage.body.findAll('p')
	#print paragraphs
	name = ""
	for p in paragraphs:
		if not name and name != "":
			return name
		else:
			links = p.findAll('a', href=re.compile('^\/wiki\/(?!.*File|Help).*'))
			if links:
				name = links[0].get('href')[6:]
				return name


p = open("Path2.txt", "w")


def iterate(startName):
	#try:
		count = 0
		# Print first page
		#print (cgi.escape(startName))
		page = getFirstLink(template + cgi.escape(startName))
		#print (template + cgi.escape(startName))
		# Print second page
		print page

		if startName.lower() == "philosophy":
			return 0
		else:
			count += 1
			while page != "Philosophy":
				# Here the path can be saved or whatever

				link = template + page
				page = getFirstLink(link)
				# Print each page
				print (page)
				p.write(page + "\n")
				count += 1
			return count
	#except Exception:
		#return "inf"
	
#print iterate("Hernan Cortes")

f=open("WordList2.txt",'r')
l=open('Steps2.txt','w')
lines=f.read().splitlines()
#print lines[0]
#print iterate(lines[0])
#print lines
#print len(lines)
#print f


for i in lines:
	def signal_handler(signum, frame):
		raise Exception("Timed out!")


	signal.signal(signal.SIGALRM, signal_handler)
	signal.alarm(20)
	print i
	try:
		p.write(i + ":\n")
		k=str(iterate(i))+"\n"
		print k
		p.write("\n")
		l.write(k)
	except Exception:
		l.write("inf"+"\n")

p.close()
f.close()
l.close()