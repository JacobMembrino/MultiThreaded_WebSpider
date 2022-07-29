# first, run installs on the following software:
# $ pip install beautifulsoup4


import urllib.request
import re, sys, mechanize
import pymysql.cursors
from bs4 import BeautifulSoup

website = sys.argv[1]
depth = sys.argv[2]

request = urllib.request.urlopen(website)
my_HTML = request.read().decode("utf8")
print(my_HTML)

soup = BeautifulSoup(request, 'html.parser')

forms = soup.find_all("div")

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
