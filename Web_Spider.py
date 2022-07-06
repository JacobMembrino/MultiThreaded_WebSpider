#!/usr/bin/env python
import urllib2, sys, mechanize, pymysql.cursors
from bs4 import BeautifulSoup

proxy_setting = urllib2.ProxyHandler({'http': sys.argv[1] + ':' + sys.argv[2]})
website = sys.argv[3]
depth = sys.argv[4]

opener = urllib2.build_opener(proxy_setting)
urllib2.instal_opener(opener)
html_doc = urllib2.urlopen(website)
soup = BeautifulSoup(html_doc, 'html.parser')

forms = soup.findAll("div")
if depth == 0 :
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
            database="mydatabase")
else if depth >= 1 :
    mydb = mysql.connector.connect(
        host="localhost",
        user="usr",
        passwd="password",
            database="mydatabase")
else :
    print("Enter Valid Depth Int.")

mycursor = mydb.cursor()

for column in forms:
    form = column.find('td').text.strip()
    print(form,'\n')

    query = "INSERT INTO ROW1 (form) VALUES (%s)"
    arguments = (form)
    mycursor.execute(query, arguments)
    mydb.commit()
