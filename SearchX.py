#!/usr/bin/python2
#c0d3d by n0t3rm
import os
import requests
import sys
##################
os.system("clear")
##################
#C0d3d by n0t3rm



"""
USE: python SearchX.py <URL> common.txt
"""


url = sys.argv[1]
arquivo = open(sys.argv[2])

logo = """\t\t\n\033[1;34m

  ,_
 ,'  `\,_
 |_,-'_)
 /##c '\  (      <> SearchX<>
' |'  -{.  )     <> Dev: n0t3rm<>
 /\__-' \[]      <> Telegram: @n0term
 /`-_`\
 '     \

\033[0;0m"""
print logo
print "\033[1;30m[\033[1;31m+\033[1;30m]\033[0;0m"*35
######################




headers = {
	'User-Agent': 'Google Chrome Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36.',
}

try:
	for linhas in arquivo:
	    linhas = linhas.rstrip('\n')
	    link = url+ linhas+'/'
	    request = requests.get(link, headers=headers)
	    status = request.status_code
	    if status == 200:
	        print "[\033[32m\033[1m+\033[0;0m] %s ==> encontrado!"%(link)
	    elif status == 403:
	        print "[\033[33m\033[1m!\033[0;0m] %s ==> acesso negado!"%(link)
except:
	print "[\033[1;31m-\033[0;0m] ocorreu um erro!"

####
